// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

// This is a simplified version of ERC20 implementation.

// ERC20 is a technical standard used for smart contracts on
// the Ethereum blockchain that govern the implementation of fungible tokens.


contract ERC20 {
    mapping(address => uint256) private _balances;

    mapping(address => mapping(address => uint256)) private _allowances;

    uint256 public totalSupply;

    string private _name;
    string private _symbol;


    constructor(string memory name_, string memory symbol_) {
        _name = name_;
        _symbol = symbol_;
    }

    function name() public view virtual returns (string memory) {
        return _name;
    }

    function symbol() public view virtual returns (string memory) {
        return _symbol;
    }

    function decimals() public pure returns (uint256) {
        return 18;
    }

    function balanceOf(address account) public view returns (uint256) {
        return _balances[account];
    }

    function transfer(address to, uint256 amount) public virtual returns (bool) {
        address owner = _msgSender();
        _transfer(owner, to, amount);
        return true;
    }

    function allowance(address owner, address spender) public view returns (uint256) {
        return _allowances[owner][spender];
    }

    function approve(address spender, uint256 amount) public returns (bool) {
        address owner = _msgSender();
        _approve(owner, spender, amount);
        return true;
    }

    function transferFrom(address from, address to, uint256 amount) public returns (bool) {
        address spender = _msgSender();
        _spendAllowance(from, spender, amount);
        _transferFrom(from, to, amount);
        return true;
    }

    function _spendAllowance(address owner, address spender, uint256 amount) internal {
        uint256 currentAllowance = allowance(owner, spender);
        require(currentAllowance >= amount, "ERC20: Insufficient Allowance.");
        _approve(owner, spender, currentAllowance - amount);
    }

    function _approve(address owner, address spender, uint256 amount) internal virtual {
        require(owner != address(0), "ERC20: Address Not Allowed.");
        require(spender != address(0), "ERC20: Address Not Allowed.");

        _allowances[owner][spender] = amount;
    }

    function _transferFrom(address from, address to, uint256 amount) internal {
        require(from != address(0), "ERC20: Address Not Allowed.");
        require(to != address(0), "ERC20: Address Not Allowed.");

        uint256 fromBalance = _balances[from];
        require(fromBalance >= amount, "ERC20: Insufficient Balance.");
        _balances[from] = fromBalance - amount;
        _balances[to] += amount;
    }

    function increaseAllowance(address spender, uint256 addedValue) public returns (bool) {
        address owner = _msgSender();
        _approve(owner, spender, allowance(owner, spender) + addedValue);
        return true;
    }

    function decreaseAllowance(address spender, uint256 subtractedValue) public returns (bool) {
        address owner = _msgSender();
        uint256 currentAllowance = allowance(owner, spender);
        require(currentAllowance >= subtractedValue, "ERC20: Insufficient Allowance.");
        _approve(owner, spender, currentAllowance - subtractedValue);
        return true;
    }

    function _transfer(address from, address to, uint256 amount) internal {
        require(from != address(0), "ERC20: Address Not Allowed.");
        require(to != address(0), "ERC20: Address Not Allowed.");

        uint256 fromBalance = _balances[from];
        require(fromBalance - amount >= 0, "ERC20: Insufficient Balance.");
        _balances[from] = fromBalance - amount;
        _balances[to] += amount;
    }

    function _mint(address account, uint256 amount) internal virtual {
        require(account != address(0), "ERC20: Address Not Allowed.");
        totalSupply += amount;
        _balances[account] += amount;
    }

    function _burn(address account, uint256 amount) internal virtual {
        require(account != address(0), "ERC20: Address Not Allowed.");
        uint256 accountBalance = _balances[account];
        require(accountBalance >= amount, "ERC20: Insufficient Balance.");
        _balances[account] = accountBalance - amount;
        totalSupply -= amount;
    }

    function _msgSender() internal view returns (address) {
        return msg.sender;
    }
}
