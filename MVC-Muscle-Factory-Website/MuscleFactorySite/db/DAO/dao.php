<?php
/**
 * @author: luca
 * Base class for DAOs
 */
class BaseDAO {
	
	var $dbManager = null;
	
	//--Function declared as based DAO  which assigns the DBManager which is attained from the simple_db_manager script
	function BaseDAO($dbMng) {
		$this->dbManager = $dbMng;	
	}
	
	function getDbManager() {
		return $this->dbManager;
	}
}

?>
