<?php

//same as the authentication_factory this is used to pass variables between controller and db
//then routed back to the view depending on the controller.

include_once './conf/config.inc.php';
include_once './db/DAO_factory.php';
include_once 'validation_factory.php';
include_once 'authentication_factory.php';

class Model {
	public $DAO_Factory, $validationFactory, $authenticationFactory; // factories
	private $usersDAO, $contentDAO; // DAOs
	public $appName = "", $introMessage = "", $loginStatusString = "", $rightBox = "",$displayTables = "",$deleteCurrentUserSuc = "", $signUpConfirmation = "",$middleBox = "", $allUsers = "", $allRecords = "",$nonLoggedInUserRec="",$nonLoggedInUser="",$searchResults=""; // strings
	public $newUserErrorMessage = "", $authenticationErrorMessage = "";	//error messages
	public $hasAuthenticationFailed = false, $hasRegistrationFailed=null;	//control variables
	
	public function __construct() {
		$this->DAO_Factory = new DAO_Factory ();
		$this->DAO_Factory->initDBResources ();
		$this->usersDAO = $this->DAO_Factory->getUsersDAO ();
		$this->authenticationFactory = new authentication_factory ( $this->usersDAO );
		$this->validationFactory = new validation_factory ();
		$this->appName = APP_NAME;
		$this->contentDAO = $this->DAO_Factory->getContentDAO();
	}
	public function nonLoggedIn(){
		$this->nonLoggedInUserRec = NOT_LOGGED_IN_STRING;
		$this->nonLoggedInUser = USERS_NOT_LOGGED_IN;
	}
	public function deleteCurUser(){
		$this->deleteCurrentUserSuc = USER_DELETED_STRING;
	}
	public function loginUser($userID, $username,$fullname) {
		$this->authenticationFactory->loginUser ( $userID, $username, $fullname );
	}
	public function getUserPasswordDigest($username) {
		return ($this->usersDAO->getUserPasswordDigest ( $username ));
	}
	public function getUserID($username) {
		return ($this->usersDAO->getUserId ( $username ));
	}
	public function getUserFullName($username) {
		return ($this->usersDAO->getUserFullName ( $username ));
	}
	public function getAllUsers(){
		$this->allUsers =  $this->usersDAO->getAllUsers();
	}	
	public function getAllExercises(){
		$this->allRecords = $this->contentDAO->getAllExercises();
	}	
	public function search($parameters){
		$this->searchResults = $this->contentDAO->searchResults($parameters);
	}
	public function prepareIntroMessage() {
		$this->introMessage = INDEX_INTRO_MESSAGE_STR;
	}
	public function setUpNewUserError($errorString) {
		$this->newUserErrorMessage = "<div class='alert alert-error'>" . $errorString . "</div>";
	}
	public function updateLoginStatus() {
		$this->loginStatusString = LOGIN_USER_FORM_WELCOME_STR . " " . $this->authenticationFactory->getFullnameLoggedIn () . " | " . LOGIN_USER_FORM_LOGOUT_STR;
		$this->authenticationErrorMessage = "";
	}
	public function updateLoginErrorMessage() {
		$this->authenticationErrorMessage = LOGIN_USER_FORM_AUTHENTICATION_ERROR;
		$this->loginStatusString = "";
	}
	public function setConfirmationMessage(){
		$this->signUpConfirmation = REGISTRATION_COMPLETE;
	}
	public function insertNewUser($username,$email, $hashedPassword,$fullname) {
		return ($this->usersDAO->insertNewUser ( $username,$email, $hashedPassword, $fullname));
	}
	public function updateUser($username,$password,$email){
		$hashedPassword = hash ( "sha1", $password );
		$this->usersDAO->updateUser($username,$hashedPassword,$email);
	}
	public function updateExercise($ID,$Exercise,$Description,$Type){
		$this->contentDAO->updateExercise($ID,$Exercise,$Description,$Type);
	}
	public function logoutUser() {
		$this->authenticationFactory->logoutUser ();
		$this->loginStatusString = null;
		$this->authenticationErrorMessage = "";
	}
	public function isUserLoggedIn() {
		return ($this->authenticationFactory->isUserLoggedIn ());
	}
	public function __destruct() {
		$this->DAO_Factory->clearDBResources ();
	}
	
	public function insertNewExercise($ex_name, $ex_desc,$type) {
		return ($this->contentDAO->insertNewExercise( $ex_name, $ex_desc,$type ));
	}    
	public function deleteExercise($ex_id){
		$this->contentDAO->deleteExercise($ex_id);
	}
	public function deleteUser($username){
		$this->usersDAO->deleteUser($username);
	}
}
?>