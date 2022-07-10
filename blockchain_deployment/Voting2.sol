pragma solidity ^0.8.0;

contract Voting2 {
    address payable  winner ;
    address [] public voters_list;
    address[] internal voters_already_voted ;
    address public owner  ;
    bool public vote = true  ;
    address[] internal funders ;

    constructor(address _winner, address[] memory _voters_list){
        winner = payable(_winner) ;
        owner = msg.sender ;
        voters_list = _voters_list ;
    }

    function fund() public payable {
        funders.push(msg.sender);
    }

    modifier onlyOwner(){
        require(msg.sender == owner) ;
        _;
    }

    function voting(bool _vote) public{
        bool check = true ;

        // checking if the voter already voted or not
        for(uint256 index = 0 ; index < voters_already_voted.length ; index++){
            if(msg.sender == voters_already_voted[index]){
                check = false ;
            }
        }

        // checking voters list
        for(uint256 index = 0 ; index < voters_list.length ; index++){
            if(msg.sender != voters_list[index]){
                check = false ;
            }
            else {
                check = true ;
                voters_already_voted.push(msg.sender);
                break ;// voter is found!
            }
        }

        if(check && vote){
            vote = _vote  ;
        }
    }

    /*
    @notice Checks if every vote given was +ve or not
    */
    function withdraw() public onlyOwner{
        if (vote){
            address payable winner2 = payable(winner) ;
            winner2.transfer(address(this).balance) ;
        }
    }

}
