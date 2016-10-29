<?php
//this is used to bring the MVC togather and bring it to the browser
//Also a session is started/resumed
$action = "";
if (! empty ( $_REQUEST ['action'] ))
	$action = $_REQUEST ['action'];

include "models/Model.php";
include "controllers/Controller.php";
include "views/View.php";

$model = new Model ();
$controller = new Controller ( $model, $action, $_REQUEST );
$view = new View ( $controller, $model );
$view->output ();

?>

