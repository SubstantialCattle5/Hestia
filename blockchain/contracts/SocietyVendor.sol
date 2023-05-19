//SPDX-License-Identifier:MIT
pragma solidity ^0.8.0;

contract SocietyVendorContract {
    struct Request {
        uint id;
        address society;
        string description;
        uint deadline;
        uint budget;
    }

    struct Tender {
        uint id;
        uint requestId;
        address vendor;
        uint amount;
        string description;
    }
    uint public timeLimit;
    Request public request;
    Tender public tender;
    uint public amount;
    bool public taskComplete;
    bool public paymentReleased;

    constructor(
        uint _timeLimit,
        Request memory _request,
        Tender memory _tender
    ) payable {
        timeLimit = _timeLimit;
        request = _request;
        tender = _tender;
        amount = msg.value;
    }

    function verifyTaskCompletion() public {
        //!FEAT: Add logic for verifying task completion by a third party
        taskComplete = true;
    }

    function releasePayment() public {
        require(taskComplete, "Task must be complete before releasing payment");
        require(!paymentReleased, "Payment has already been released");
        // Transfer funds from contract to vendor
        payable(tender.vendor).transfer(amount);
        paymentReleased = true;
    }
}

contract SocietyVendor {
    mapping(address => bool) public isSociety;
    mapping(address => bool) public isVendor;

    modifier onlySociety() {
        require(isSociety[msg.sender], "Only societies can call this function");
        _;
    }

    modifier onlyVendor() {
        require(isVendor[msg.sender], "Only vendors can call this function");
        _;
    }

    function registerSociety() public {
        isSociety[msg.sender] = true;
    }

    function registerVendor() public {
        isVendor[msg.sender] = true;
    }

    struct Request {
        uint id;
        address society;
        string description;
        uint deadline;
        uint budget;
    }

    struct Tender {
        uint id;
        uint requestId;
        address vendor;
        uint amount;
        string description;
    }

    struct Vote {
        uint tenderId;
        address voter;
        uint timestamp;
    }

    struct Contract {
        SocietyVendorContract contractInstance;
        address society;
        address vendor;
        uint amount;
        uint requestId;
        uint tenderId;
    }

    mapping(uint => Request) public requests;
    mapping(uint => Tender) public tenders;
    mapping(uint => Vote[]) public votesByTender;
    mapping(address => mapping(uint => bool)) public hasVoted;
    mapping(uint => Tender[]) public tendersByRequest;
    mapping(uint => Contract) public contractsByRequest;

    uint public requestCount;
    uint public tenderCount;

    event RequestCreated(uint requestId);
    event TenderCreated(uint tenderId);

    function createRequest(
        string memory _description,
        uint _deadline,
        uint _budget
    ) public onlySociety {
        Request memory newRequest = Request(
            requestCount,
            msg.sender,
            _description,
            _deadline,
            _budget
        );
        requests[requestCount] = newRequest;
        requestCount++;
        emit RequestCreated(newRequest.id);
    }

    function createTender(
        uint _requestId,
        uint _amount,
        string memory _description
    ) public onlyVendor {
        Tender memory newTender = Tender(
            tenderCount,
            _requestId,
            msg.sender,
            _amount,
            _description
        );
        tenders[tenderCount] = newTender;
        tendersByRequest[_requestId].push(newTender);
        tenderCount++;
        emit TenderCreated(newTender.id);
    }

    function castVote(uint _tenderId) public {
        require(
            !hasVoted[msg.sender][_tenderId],
            "You have already voted for this tender"
        );
        Vote memory newVote = Vote(_tenderId, msg.sender, block.timestamp);
        votesByTender[_tenderId].push(newVote);
        hasVoted[msg.sender][_tenderId] = true;
    }

    function selectWinner(
        uint _requestId,
        uint minVotes
    ) public view onlySociety returns (Tender memory, Request memory) {
        require(
            requests[_requestId].society == msg.sender,
            "Only the society that created the request can select a winner"
        );
        uint maxVotes = 0;
        uint winningTenderId;
        for (uint i = 0; i < tendersByRequest[_requestId].length; i++) {
            uint tenderId = tendersByRequest[_requestId][i].id;
            uint numVotes = votesByTender[tenderId].length;
            if (numVotes >= minVotes && numVotes > maxVotes) {
                maxVotes = numVotes;
                winningTenderId = tenderId;
            }
        }
        // Handle the winning tender
        Tender memory winningTender = tenders[winningTenderId];
        Request memory request = requests[_requestId];

        return (winningTender, request);
    }

    function deployContract(
        uint _requestId,
        uint _tenderId,
        uint _timeLimit,
        uint _amount
    ) public payable onlySociety {
        require(
            requests[_requestId].society == msg.sender,
            "Only the society that created the request can deploy a contract"
        );
        require(
            msg.value == _amount,
            "The amount sent must match the specified amount"
        );
        Tender memory selectedTender = tenders[_tenderId];
        SocietyVendorContract.Tender memory tender = SocietyVendorContract
            .Tender(
                selectedTender.id,
                selectedTender.requestId,
                selectedTender.vendor,
                selectedTender.amount,
                selectedTender.description
            );
        SocietyVendorContract.Request memory request = SocietyVendorContract
            .Request(
                requests[_requestId].id,
                requests[_requestId].society,
                requests[_requestId].description,
                requests[_requestId].deadline,
                requests[_requestId].budget
            );
        // Deploy new instance of contract with specified time limit and amount
        SocietyVendorContract newContract = new SocietyVendorContract{
            value: _amount
        }(_timeLimit, request, tender);
        // Store contract in mapping
        Contract memory contractInstance = Contract(
            newContract,
            request.society,
            tender.vendor,
            _amount,
            request.id,
            tender.id
        );
        contractsByRequest[_requestId] = contractInstance;
    }

    function getTendersForRequest(
        uint _requestId
    ) public view returns (Tender[] memory) {
        return tendersByRequest[_requestId];
    }

    function getTender(uint _tenderId) public view returns (Tender memory) {
        return tenders[_tenderId];
    }

    function getRequest(uint _requestId) public view returns (Request memory) {
        return requests[_requestId];
    }

    function getNumberOfVotes(uint _tenderId) public view returns (uint) {
        return votesByTender[_tenderId].length;
    }

    function getContractDetails(
        uint _requestId
    ) public view returns (Contract memory) {
        return contractsByRequest[_requestId];
    }

    function editRequest(
        uint _requestId,
        string memory _description,
        uint _deadline,
        uint _budget
    ) public onlySociety {
        require(
            requests[_requestId].society == msg.sender,
            "Only the society that created the request can edit it"
        );
        requests[_requestId].description = _description;
        requests[_requestId].deadline = _deadline;
        requests[_requestId].budget = _budget;
    }
}
