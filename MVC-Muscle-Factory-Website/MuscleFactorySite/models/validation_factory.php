<?php

//this is used to ensure the lengths of the strings are right for the db
//also used to ensure the email structure is right for a valid email
class validation_factory {

	public function isEmailValid($emailStr){
		$regex = "/^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$/i";
		if(!preg_match($regex, $emailStr)) return (false);
		else return (true);
	}
	public function isLengthStringValid($string, $maxchars){
		if (is_string($string))
			if (strlen($string)<=$maxchars) return (true);	

		return (false);
	}
}
?>