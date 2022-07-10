//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Voting {
    address public winner ;
    uint256 public money ;
    string public problem ;
    address[] internal voters ;
    address public owner ;
    uint256 public vote_sum ;
    bool public paying_check ;


    constructor(address _winner , uint256 _money) public {
        winner = _winner ;
        money = _money ;
        owner = msg.sender;
    }
    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }


    /*
        function1
        @param : flag - tells if the vote is +ve or -ve
        @return : nothing
        @notice : votes on the solution and pushes the user user_address to the list
    */
    function vote(bool _flag) public{
        bool flag = true ;
        for(uint256 index = 0 ; index <voters.length ; index++){
           if(msg.sender == voters[index]){
               flag = false ;
               break ;
           }
        }
        // Check
        if (flag){
            if(paying_check){
                paying_check = _flag  ;
            }
        voters.push(msg.sender) ;
        }

    }

    /*
    @notice Checks if every vote given was +ve or not
    */
    function withdraw(uint256 judges) public onlyOwner{
        if (paying_check){
            address payable winner2 = payable(winner) ;
            winner2.transfer(address(this).balance) ;
        }
    }


}
