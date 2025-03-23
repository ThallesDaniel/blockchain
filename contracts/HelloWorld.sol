pragma solidity ^0.8.7;

contract HelloWorld {
    // string public message = "Hello, World!";
    
    // function update(string memory newMessage) public {
    //     message = newMessage;
    // }
    uint public number = 0;

    function setInt(uint _number)public{
        number = _number;
    }

}