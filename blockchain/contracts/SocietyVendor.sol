pragma solidity ^0.8.0;

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

    mapping(uint => Request) public requests;
    mapping(uint => Tender) public tenders;
    uint public requestCount;
    uint public tenderCount;

    mapping(uint => Tender[]) public tendersByRequest;

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
}
