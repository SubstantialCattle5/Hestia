# Solidity API

## SocietyVendorContract

### Request

```solidity
struct Request {
  uint256 id;
  address society;
  string description;
  uint256 deadline;
  uint256 budget;
}
```

### Tender

```solidity
struct Tender {
  uint256 id;
  uint256 requestId;
  address vendor;
  uint256 amount;
  string description;
}
```

### timeLimit

```solidity
uint256 timeLimit
```

### request

```solidity
struct SocietyVendorContract.Request request
```

### tender

```solidity
struct SocietyVendorContract.Tender tender
```

### amount

```solidity
uint256 amount
```

### taskComplete

```solidity
bool taskComplete
```

### paymentReleased

```solidity
bool paymentReleased
```

### constructor

```solidity
constructor(uint256 _timeLimit, struct SocietyVendorContract.Request _request, struct SocietyVendorContract.Tender _tender) public payable
```

### verifyTaskCompletion

```solidity
function verifyTaskCompletion() public
```

### releasePayment

```solidity
function releasePayment() public
```

## SocietyVendor

### isSociety

```solidity
mapping(address => bool) isSociety
```

### isVendor

```solidity
mapping(address => bool) isVendor
```

### onlySociety

```solidity
modifier onlySociety()
```

### onlyVendor

```solidity
modifier onlyVendor()
```

### registerSociety

```solidity
function registerSociety() public
```

### registerVendor

```solidity
function registerVendor() public
```

### Request

```solidity
struct Request {
  uint256 id;
  address society;
  string description;
  uint256 deadline;
  uint256 budget;
}
```

### Tender

```solidity
struct Tender {
  uint256 id;
  uint256 requestId;
  address vendor;
  uint256 amount;
  string description;
}
```

### Vote

```solidity
struct Vote {
  uint256 tenderId;
  address voter;
  uint256 timestamp;
}
```

### Contract

```solidity
struct Contract {
  contract SocietyVendorContract contractInstance;
  address society;
  address vendor;
  uint256 amount;
  uint256 requestId;
  uint256 tenderId;
}
```

### requests

```solidity
mapping(uint256 => struct SocietyVendor.Request) requests
```

### tenders

```solidity
mapping(uint256 => struct SocietyVendor.Tender) tenders
```

### votesByTender

```solidity
mapping(uint256 => struct SocietyVendor.Vote[]) votesByTender
```

### hasVoted

```solidity
mapping(address => mapping(uint256 => bool)) hasVoted
```

### tendersByRequest

```solidity
mapping(uint256 => struct SocietyVendor.Tender[]) tendersByRequest
```

### contractsByRequest

```solidity
mapping(uint256 => struct SocietyVendor.Contract) contractsByRequest
```

### requestCount

```solidity
uint256 requestCount
```

### tenderCount

```solidity
uint256 tenderCount
```

### RequestCreated

```solidity
event RequestCreated(uint256 requestId)
```

### TenderCreated

```solidity
event TenderCreated(uint256 tenderId)
```

### createRequest

```solidity
function createRequest(string _description, uint256 _deadline, uint256 _budget) public
```

### createTender

```solidity
function createTender(uint256 _requestId, uint256 _amount, string _description) public
```

### castVote

```solidity
function castVote(uint256 _tenderId) public
```

### selectWinner

```solidity
function selectWinner(uint256 _requestId, uint256 minVotes) public view returns (struct SocietyVendor.Tender, struct SocietyVendor.Request)
```

### deployContract

```solidity
function deployContract(uint256 _requestId, uint256 _tenderId, uint256 _timeLimit, uint256 _amount) public payable
```

### getTendersForRequest

```solidity
function getTendersForRequest(uint256 _requestId) public view returns (struct SocietyVendor.Tender[])
```

### getTender

```solidity
function getTender(uint256 _tenderId) public view returns (struct SocietyVendor.Tender)
```

### getRequest

```solidity
function getRequest(uint256 _requestId) public view returns (struct SocietyVendor.Request)
```

### getNumberOfVotes

```solidity
function getNumberOfVotes(uint256 _tenderId) public view returns (uint256)
```

### getContractDetails

```solidity
function getContractDetails(uint256 _requestId) public view returns (struct SocietyVendor.Contract)
```

### editRequest

```solidity
function editRequest(uint256 _requestId, string _description, uint256 _deadline, uint256 _budget) public
```

