<?php

//This handles sql queries regarding the user
//used for updating data in the db, obtaining id,uname,password ect



require_once("dao.php");
class usersDAO extends BaseDAO {

	function messagesDAO($dbMng) {
		parent::BaseDAO($dbMng);
	}
	
	//used for login and updating
	public function isUserExisting($username){
		$sqlQuery = "SELECT count(*) as isExisting ";

		$sqlQuery .= "FROM user_table ";

		$sqlQuery .= "WHERE user_name='$username' ";		
		//Calls the method from the DAOFactory and passes in the query to be  execute, and the result is stored
		$result = $this->getDbManager()->executeSelectQuery($sqlQuery);
		
		if ($result[0]["isExisting"] == 1) return (true);

		else return (false);
	}
	
	public function updateUser($username,$hashedPassword,$email){
		
		$sqlQuery = "UPDATE user_table ";
		$sqlQuery .= "SET user_name='$username' , password='$hashedPassword' , email='$email' ";
		$sqlQuery .= "WHERE user_name='$username' ";
		$result = $this->getDbManager()->executeQuery($sqlQuery);
		
		
	}
	//this is for putting id in the SESSION
	public function getUserId($username){

		$sqlQuery = "SELECT user_id ";

		$sqlQuery .= "FROM user_table ";
		$sqlQuery .= "WHERE user_name='$username' ";	
		$result = $this->getDbManager()->executeSelectQuery($sqlQuery);
			

		if (!empty($result[0]["user_id"])) return ($result[0]["user_id"]);

		else return (false);

	}
	//this is for the nav bar on the right for when the user has logged in
		public function getUserFullName($username){

		$sqlQuery = "SELECT full_name ";

		$sqlQuery .= "FROM user_table ";
		$sqlQuery .= "WHERE user_name='$username' ";	
		
		$result = $this->getDbManager()->executeSelectQuery($sqlQuery);
			

		if (!empty($result[0]["full_name"])) return ($result[0]["full_name"]);

		else return (false);

	}
	
	public function getAllUsers(){
	
		$sqlQuery = "SELECT * ";
		$sqlQuery .= "FROM user_table ";
		
		$result = $this->getDbManager()->executeSelectQuery($sqlQuery);
		
		return $result; 
	}
	
	public function deleteUser($username){
		$sqlQuery = "DELETE FROM user_table ";
		$sqlQuery .= "WHERE user_name = '$username' ";		
		$result = $this->getDbManager()->executeQuery($sqlQuery);
	
	}
	
	//used for the encryption
	
	public function getUserPasswordDigest($username) {
		$sqlQuery = "SELECT password ";
		$sqlQuery .= "FROM user_table ";
		$sqlQuery .= "WHERE user_name='$username' ";
		$result = $this->getDbManager()->executeSelectQuery($sqlQuery);
		if ($result != NULL) return $result[0]["password"];
		return (NULL);
	}
	
	public function insertNewUser($username,$email, $passwordHash,$fullname) {
		$sqlQuery = "INSERT INTO user_table (user_name,email, password, full_name) ";
	$sqlQuery .= "VALUES ('$username','$email', '$passwordHash', '$fullname') ";
		$result = $this->getDbManager()->executeQuery($sqlQuery);

		return $result;
	}
	
	
}
?>