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
    address[] public voters_list ;


    constructor(address _winner , uint256 _money , address[] memory _voters) public {
        winner = payable(_winner) ;
        money = _money ;
        owner = msg.sender;
        voters_list = _voters ;

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
        // check if the voter has already voted
        for(uint256 index = 0 ; index <voters.length ; index++){
           if(msg.sender == voters[index]){
               flag = false ;
               break ;

           }
        }
        // check for voter list names
        for(uint256 index = 0 ; index <voters_list.length ; index++){
           if (msg.sender != voters_list[index]){
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
    function withdraw() public onlyOwner{
        if (paying_check){
            address payable winner2 = payable(winner) ;
            winner2.transfer(address(owner).balance) ;
        }
    }


}
