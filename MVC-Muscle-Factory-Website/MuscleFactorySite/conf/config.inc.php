<?php
// These are values that are used accross the MVC
define("DB_HOST", "localhost" ); 		
define("DB_USER", "root" ); 			
define("DB_PASS", "" ); 		
define("DB_PORT", 3306);				
define("DB_NAME", "webdev_assignment" ); 		
define("APP_NAME", "Muscle Factory" );
define ( "FOOTER", "Fionn Mcguire C13316356, Micheal Slattery C12383326, Group X" );	

//Error messages
define("FORM_ERROR_STRING", "Errors exist in the form");
define("FORM_DETAILS_STRING", "All Details Must be filled in");
define("FORM_USER_EXISTS_STRING", "Another user already exists in the system with the same username");
define("REGISTRATION_COMPLETE", "Registration success");
define("REG_ERROR", "Error with registration");
define("NOT_LOGGED_IN_STRING","Cannot alter information without being logged in");
define("USERS_NOT_LOGGED_IN","You must be logged in before editing information");
define("USER_DELETED_STRING","Delete success");
define("LOGIN_USER_FORM_WELCOME_STR", "Welcome");
define("LOGIN_USER_FORM_AUTHENTICATION_ERROR", "Sorry, Incorrect Details.");

//Max login constraints to ensure we dont get an sql error
define("LOGIN_USER_FORM_MAX_USERNAME_LENGTH", 30);	
define("LOGIN_USER_FORM_MAX_PASSWORD_LENGTH", 20); 	
define("LOGIN_USER_FORM_LOGOUT_STR", "Logout");
define("MAX_LENGTH_USERNAME", 30);	
define("MAX_PASSWORD_LEN", 20); 
define("MAX_FULLNAME_LEN", 80); 


define("INDEX_INTRO_MESSAGE_STR", " " . APP_NAME. "");
define("LOGGED_IN_USER_MENU", "<ul><li>option 1</li><li>option 2 </li></li>");
define("USER_NOT_LOGGED_IN","You cannot work out until you log in");
?>