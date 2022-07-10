//SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract Suggestion {
    address public  owner ;
    string public problem ;

    /*
        Problem - Buy more Benches

        Solution 1 :
        1) Name
        2) Address
        3) Solution : Buy 5 yellow benches
        4) Cost
        5) Vote


        */

    struct tasks{
        address user ;
        string name ;
        string solution ;
        uint256 cost ;
        int256 votes ;
    }


    /*
     User Address ====> tasks
    */
    mapping(address => tasks) public task ;
    // list of voters
    address[] internal voters ;

    constructor(string memory _problem) public {
            owner = msg.sender;
            problem = _problem ;
    }

    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }

    /* function 1 - creates a new solution
        @param : name , solution , cost , votes
        @return : user name
        @notice :
        - first checks if the user hasn't already given his a solution
        - then initializes a new task

    */
    function newsolution(
        string memory _name ,
        string memory _solution ,
        uint256 _cost
    ) public{
        bool flag = true ;
        for(uint256 index = 0 ; index < voters.length ; index++){
            if(voters[index] == msg.sender) {
                flag = false ;
                break ;
            }
        }
        if (flag==true){
        task[msg.sender] = tasks(msg.sender , _name , _solution , _cost , 0) ;
        voters.push(msg.sender) ; }
        else{
        task[msg.sender] = tasks(msg.sender , _name , _solution , _cost , task[msg.sender].votes) ;
    }
    }


    /*
        function2
        @param : flag - tells if the vote is +ve or -ve
        @return : nothing
        @notice : votes on the solution
    */
    function uservote(bool _flag , address _candiate) public {
        if(_flag) {
            task[_candiate].votes += 1 ;
        }
        else if(!_flag) {
            task[_candiate].votes -= 1 ;
        }

    }

    /*
        function3
        @param : none
        @return : address of the winning suggestion can return none
        @notice : returns the winner -- only owner can call it
    */
    function endsuggestion() public onlyOwner returns(address winner){
        require(voters.length > 0) ;
        address checkaddress; // can @return none
        int checkvote = 0  ;
        for(uint256 index = 0 ; index < voters.length ; index++){
            if(checkvote < task[voters[index]].votes){
                checkvote = task[voters[index]].votes ;
                checkaddress = voters[index];
            }
        }
        winner = checkaddress ;
    }

}
