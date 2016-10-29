<?php

//this is used for passing authentication function of the login/logout, encryption & checking the status of the user
//this is also used to return the values which have been returned from the db functions
//the authentication_factory and the other model files
//are used to pass variables to and from the control and db files

class authentication_factory {
	private $usersDAO;
	public function __construct($usersDAO) {
		$this->usersDAO = $usersDAO;
	}
	public function isUserExisting($username) {
		return ($this->usersDAO->isUserExisting ( $username ));
	}
	
	public function insertNewUser($username, $password) {
		$hashedPassword = hash ( "sha1", $password );
		return ($this->usersDAO->insertNewUser ( $username, $hashedPassword ));
	}
	public function getHashValue($string) {
		return (hash ( "sha1", $string ));
	}
	public function loginUser($userId, $username, $fullname) {
		$_SESSION ['user_id'] = $userId;
		$_SESSION ['user_name'] = $username;
		$_SESSION ['full_name'] = $fullname;
	}
	public function isUserLoggedIn() {
		return (! empty ( $_SESSION ['user_id'] ));
	}
	public function getUsernameLoggedIn() {
		if ($this->isUserLoggedIn ())
			return $_SESSION ['user_name'];
		
		return (null);
	}
	public function getFullnameLoggedIn() {
		if ($this->isUserLoggedIn ())
			return $_SESSION ['full_name'];
		
		return (null);
	}
	public function logoutUser() {
		unset ( $_SESSION ['user_id'] );
		unset ( $_SESSION ['user_name'] );
		session_destroy ();
	}
}
?>