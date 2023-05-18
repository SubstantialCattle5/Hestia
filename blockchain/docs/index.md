# Solidity API

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

### requests

```solidity
mapping(uint256 => struct SocietyVendor.Request) requests
```

### tenders

```solidity
mapping(uint256 => struct SocietyVendor.Tender) tenders
```

### requestCount

```solidity
uint256 requestCount
```

### tenderCount

```solidity
uint256 tenderCount
```

### tendersByRequest

```solidity
mapping(uint256 => struct SocietyVendor.Tender[]) tendersByRequest
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

### getTendersForRequest

```solidity
function getTendersForRequest(uint256 _requestId) public view returns (struct SocietyVendor.Tender[])
```

### getTender

```solidity
function getTender(uint256 _tenderId) public view returns (struct SocietyVendor.Tender)
```

