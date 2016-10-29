<?php

//used to control the view of the app in the browser
//uses variables from the model created by the controller and db
class View {
	private $model;
	private $controller;
	
	public function __construct($controller, $model) {
		$this->controller = $controller;
		$this->model = $model;
	}
	
	//this takes template files and makes them variables so you can slot them into the page
	//there are also a few other variables which use these template variables so we were able
	//change the values in if statements when we print them to the screen
	//we then check if one of the buttons on the left is clicked to change the rightbox and middlebox
	//the right and middle are set intitially if nothing is clicked or if the user just gets
	//to the website or if they have just logged in.
	//then there are a series of if statements checking if a button has been clicked
	//upon click the button changes the right and middle button
	//this also handles the search and the registration messages
	//also used to limit the users ability without loggin in
	public function output() {
		$appName = $this->model->appName;
		$introMessage = $this->model->introMessage;
		$newUserErrorMessage = $this->model->newUserErrorMessage;
		
		$username = "";
		
		$loginBox = "";
		$authenticationErrorMessage = "";
		$rightBox = "";
		$middleBox = "";
		$confirmationMessage = "";
		$displayTables = "";
		$tableChoice = null;
		$footer = FOOTER;
		
		if ($this->model->loginStatusString != null) {
			$loginBox = "<a class='brand' href='index.php?action=logout'>" . $this->model->loginStatusString . "</a>";
			$updateUserForm = file_get_contents('./templates/update_user_form.php');
			$updateExerciseForm = file_get_contents('./templates/update_exercise_form.php');
			$deleteExerciseForm = file_get_contents('./templates/deleteExercise.php');
			$deleteUserForm = file_get_contents('./templates/deleteUser.php');
			$registrationForm = file_get_contents('./templates/insert_new_user_form.php');
			$newExerciseForm = file_get_contents('./templates/insert_new_exercise.php');
			$userTable = file_get_contents('./templates/view_exercises.php');
			$ExerciseTable = file_get_contents('./templates/view_exercises.php');
			$username = $this->model->authenticationFactory->getUsernameLoggedIn();
			$searchForm = file_get_contents('./templates/search_form.php');
			$rightBox = $registrationForm;
			$middleBox = $newExerciseForm;
			if (isset($_POST['editUser'])){
				$username = "<h3 style='color:white' > Update Current User :<br></h3><h2 style='color:cyan'><legend>" . $username . "</legend></h2>";
				$rightBox =  $registrationForm;
				$middleBox = $username . $updateUserForm;
			}
			else if (isset($_POST['editExercise'])){
				$rightBox = $newExerciseForm;
				$middleBox = $updateExerciseForm;
			}
			else if (isset($_POST['viewExercise'])){
				$rightBox = $registrationForm;
				$middleBox = "<h3 style='color:white' > Search :<br></h3><h2 style='color:cyan'><legend>What are you looking for?</legend></h2>".$searchForm;
				
			}
			else if (isset($_POST['viewUsers'])){
				$rightBox = $registrationForm;
				$middleBox = "<h3 style='color:white' > Search :<br></h3><h2 style='color:cyan'><legend>What are you looking for?</legend></h2>".$searchForm;
				
			}
			else if (isset($_POST['deleteSection'])){
				$rightBox = $deleteExerciseForm;
				$middleBox = $deleteUserForm;
				
			}
			else
			{
				$rightBox = $registrationForm;
				$middleBox = "<h3 style='color:white' > Search :<br></h3><h2 style='color:cyan'><legend>What are you looking for?</legend></h2>" . $searchForm;
			}	
			if (isset($_POST['insertNewUser'])){
				$confirmationMessage = "<div class='alert alert-success'>" . $this->model->signUpConfirmation . "</div>";
				$rightBox = $confirmationMessage;
			}
		} else {
			$authenticationErrorMessage = "";
			if ($this->model->hasAuthenticationFailed)
				$authenticationErrorMessage = $this->model->authenticationErrorMessage;
			$loginBox = file_get_contents ( "templates/login_form.php", FILE_USE_INCLUDE_PATH );
			$rightBox = $this->model->rightBox;
			$middleBox = file_get_contents ( "templates/search_form.php", FILE_USE_INCLUDE_PATH );;
			$registrationForm = file_get_contents ( './templates/insert_new_user_form.php' );
			if (isset($_POST['editExercise'])){
				$this->model->nonLoggedIn();
				$nonRegisteredUserMessage = "<div class='alert alert-error'>" . $this->model->nonLoggedInUserRec . "</div>";
				$middleBox= $nonRegisteredUserMessage . file_get_contents ( "templates/search_form.php", FILE_USE_INCLUDE_PATH )  ;
			}
			else if(isset($_POST['editUser'])){
				$this->model->nonLoggedIn();
				$nonRegisteredUserMessage = "<div class='alert alert-error'>" . $this->model->nonLoggedInUser . "</div>";
				$middleBox= $nonRegisteredUserMessage . file_get_contents ( "templates/search_form.php", FILE_USE_INCLUDE_PATH )  ;
			}
			else{
				$middleBox = file_get_contents ( "templates/search_form.php", FILE_USE_INCLUDE_PATH );
			}	
			if(isset($_POST['search'])){
				$middleBox = file_get_contents("templates/search_form.php");
				$middleBox = file_get_contents("templates/searchresults.php");
			}
			if (! isset ( $this->model->hasRegistrationFailed )) {
				$rightBox = $registrationForm;
			} else if ($this->model->hasRegistrationFailed) {
				$rightBox = $newUserErrorMessage . $registrationForm;
			} else if ($this->model->hasRegistrationFailed == false) {
				$confirmationMessage = "<div class='alert alert-success'>" . $this->model->signUpConfirmation . "</div>";
				$rightBox = $confirmationMessage;
			}	
		}
		include_once ("templates/template_index.php");
	}
}
?>