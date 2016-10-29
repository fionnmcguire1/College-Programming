<?php
require_once("dao.php");
class contentDAO extends BaseDAO{

	function messagesDAO($dbMng) {
		parent::BaseDAO($dbMng);
	}
	
	 
	public function getAllExercises(){
	
		$sqlQuery = "SELECT * ";
		$sqlQuery .= "FROM exercise_table ";
		
		$result = $this->getDbManager()->executeSelectQuery($sqlQuery);
		
		return $result; 
	}
	
	public function deleteExercise($nID){
		$sqlQuery = "DELETE FROM exercise_table ";
		$sqlQuery .= "WHERE ex_id = '$nID' ";		
		//Calls the method from the DAOFactory and passes in the query to be  execute, and the result is stored
		$result = $this->getDbManager()->executeQuery($sqlQuery);
	
	}
	
	public function searchResults($parameters){
		$sqlQuery = "SELECT * ";
		$sqlQuery .= "FROM exercise_table ";
		$sqlQuery .= " WHERE ex_id ";
		$sqlQuery .= "like '%$parameters%' OR ex_name like '%$parameters%' OR ex_desc like '%$parameters%' OR type like '%$parameters%'  ";
		
		$result = $this->getDbManager()->executeSelectQuery($sqlQuery);
		return $result;
	}
	
	public function updateExercise($nID,$nName,$nDesc,$nType){
        /*nID means new ID to hold the info that the user will input */
		
		$sqlQuery = "UPDATE exercise_table ";
		$sqlQuery .= "SET ex_name='$nName' , ex_desc='$nDesc' , type='$nType' ";
		$sqlQuery .= "WHERE ex_id='$nID' ";
		$result = $this->getDbManager()->executeQuery($sqlQuery);		
	}
	
	public function insertNewExercise($ex_name,$ex_desc,$type){
	
		$sqlQuery = "INSERT INTO exercise_table (ex_name , ex_desc , type ) ";
		$sqlQuery .= "VALUES ( '$ex_name' , '$ex_desc' , $type ) ";		
		
		$result = $this->getDbManager()->executeQuery($sqlQuery);
		return $result;
	}	


}
?>