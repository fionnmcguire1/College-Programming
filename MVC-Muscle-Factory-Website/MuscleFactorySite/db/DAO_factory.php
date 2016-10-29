<?php
include_once 'simple_db_manager.php';
class DAO_Factory {
	private $dbManager;
		function getDbManager() {
		if($this->dbManager == null)
			throw new Exception("No persistence storage link");
		return $this->dbManager;
	}
	function initDBResources() {
		$this->dbManager = new dbmanager(DB_NAME);
		$this->dbManager->openConnection();
	}
	function clearDBResources() {
		if($this->dbManager != null)
			$this->dbManager->closeConnection();
	}
	function getUsersDAO() {
		require_once("dao/usersDAO.php");
		return new usersDAO($this->getDbManager());
	}
	function getContentDAO(){
		require_once("dao/contentDAO.php");
		return new contentDAO($this->getDbManager());
	}

}


