 <?php
	class Controller {
		private $model;
		//This switch statement decides which function to execute when 
		//a form is clicked. The form id=action and then is assigned
		// a value to decide the outcome of the switch
		public function __construct($model, $action = null, $parameters) {
			$this->model = $model;
			switch ($action) {
				case "insertNewUser" :
					$this->insertNewUser ( $parameters );
					break;
				case "loginUser" :
					$this->loginUser ( $parameters );
					break;
				case "logout" :
					$this->logoutUser ();
					break;
				case "updateUser" : 
					$this->updateUser($parameters);
					break;
				case "insertNewExercise":
					$this->insertNewExercise($parameters);
					break;
				case "updateExercise":
					$this->updateExercise($parameters);
					break;
				case "viewUsers":
					$this->getAllUsers();
					break;
				case "deleteExercise":
					$this->deleteExercise($parameters);
				break;
				case "deleteUser":
					$this->deleteUser($parameters);
					break;
				case "search":
					$this->search($parameters);
					break;
				default :
					break;
			}
			
			$this->model->prepareIntroMessage ();
			$this->updateHeader ();
			$this->model->getAllUsers();
			$this->model->getAllExercises();

		}
		
		//These functions are used to send the $parameters which contain
		//a load of parameters (so we dont have to repeat ourselves)
		//The $parameters are separated and passed into one of the model files where they
		//are redirected to whichever file is going to handle the db function.
		
		function search($parameters){
			$search = $parameters['search'];
			$this->model->search($search);
		}
		
		function deleteExercise($parameters){
			$ex_id = $parameters ['exercise_id'];
			$this->model->deleteExercise($ex_id);
		
		}
		
		function deleteUser(){
			$username = $_SESSION['user_name'];
			$this->model->deleteUser($username);
		}

		//ok so this function is for inserting and took us a while but its
		//similar to the login function. first we seperate the values
		//then check if the values contain values
		//then we ensure the values are appropriote for the db/system regarding length and email structure
		//then we make sure the user is not in the db so we dont duplicate
		//then we encrypt the password
		//then we insert the values (with the encypted password) into the database
		//if the user made a mistake somewhere along the way
		//the user will be given an error message
		 
		function insertNewUser($parameters) {
			$email = $parameters ["Email"];
			$username = $parameters ["Username"];
			$password = $parameters ["Password"];
			$fullname = $parameters ["fullname"];		
			
			if (! empty ( $username ) && ! empty ( $password ) && ! empty ( $email ) && ! empty ( $fullname )) {
				if ($this->model->validationFactory->isLengthStringValid ( $username, MAX_LENGTH_USERNAME ) && $this->model->validationFactory->isLengthStringValid ( $password, MAX_PASSWORD_LEN ) && $this->model->validationFactory->isEmailValid ( $email ) && $this->model->validationFactory->isLengthStringValid ( $fullname, MAX_FULLNAME_LEN )){
					if (! $this->model->authenticationFactory->isUserExisting ( $username )) {
						$hashedPassword = $this->model->authenticationFactory->getHashValue ( $password );
						if ($this->model->insertNewUser ( $username,$email, $hashedPassword , $fullname)) {
							$this->model->hasRegistrationFailed = false;
							$this->model->setConfirmationMessage();
							return (true);
						}
						
					} else
						$this->model->setUpNewUserError ( FORM_USER_EXISTS_STRING );
				} else
					$this->model->setUpNewUserError ( FORM_ERROR_STRING );
			} else
				$this->model->setUpNewUserError ( FORM_DETAILS_STRING );
			
			$this->model->hasRegistrationFailed = true;
			$this->model->updateLoginErrorMessage ();
			return (false);
		}
		
		//This is similar to the insert
		//to confirm the login we encrypt the password the user typed in and
		//compare that to the encrypted password in the db
		//there was a problem when we were comparing the two passwords so
		//we printed the passwords and the userpassword was encrypting twice so
		//we took a shortcut and just chopped off the second encryption
		//we then compared the new_userHashedPassword to the one in the db
		//we then get the userid,username,fullname from the db according to the uname
		//ten we pass those to the login user function where they are placed in SESSION variables
		
		function loginUser($parameters) {
			$username = $parameters ["Username"];
			$password = $parameters ["Password"];
			
			if (! (empty ( $username ) && empty ( $password ))) {
				if ($this->model->validationFactory->isLengthStringValid ( $username, MAX_LENGTH_USERNAME ) && $this->model->validationFactory->isLengthStringValid ( $password, MAX_PASSWORD_LEN )) {		
                    $databaseHashedPassword = $this->model->getUserPasswordDigest ( $username );			
					$userHashedPassword = $this->model->authenticationFactory->getHashValue ( $password );
                    $new_userHashedPassword = substr($userHashedPassword, 0,20);
					if ($databaseHashedPassword == $new_userHashedPassword) {
						$userId = $this->model->getUserId ( $username );
						$fullname = $this->model->getUserFullName ( $username );
						$this->model->loginUser ( $userId, $username, $fullname );
						$this->model->updateLoginStatus ();
						$this->model->hasAuthenticationFailed = false;
						
						return;
					}
				}
			}
			$this->model->updateLoginErrorMessage ();
			$this->model->hasAuthenticationFailed = true;
			return;
		}
		function logoutUser() {
			$this->model->logoutUser ();
		}
		
		//this changes the nav bar on the right ot have a Fullname and logout button instead of a login form
		function updateHeader() {
			if ($this->model->isUserLoggedIn ())
				$this->model->updateLoginStatus ();
		}	
		function insertNewExercise($parameters) {
			$ex_name = $parameters ["ex_name"];
			$ex_desc = $parameters ["ex_desc"];
			$type = $parameters ["type"];
			
					if ($this->model->insertNewExercise( $ex_name, $ex_desc ,$type )) {
							$this->model->hasRegistrationFailed = false;
							$this->model->setConfirmationMessage();
							return (true);
						}
		}	
		function updateUser($parameters){
			$username = $_SESSION['user_name'];
			$password = $parameters["Password"];
			$email = $parameters["Email"];
			
			$this->model->updateUser($username,$password,$email);
		}
		function updateExercise($parameters){
			$exID = $parameters["ID"];
			$exName = $parameters["Exercise"];
			$exDesc = $parameters["Description"];
			$exType = $parameters["Type"];
			$this->model->updateExercise($exID,$exName,$exDesc,$exType);
		}		
	}
	?>