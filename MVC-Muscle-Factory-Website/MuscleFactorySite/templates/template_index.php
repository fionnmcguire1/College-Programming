<!DOCTYPE html>
<?php include_once 'html_doctype_and_head.php'; ?>
<body>

<?php ?>
	<div class="container-fluid">
		<div class="row-fluid" style="margin-top: 50px">
		
		
		
			<div class='span6'style=" background:rgba(255,255,255,0.3);">
					
					<div>
					<div class="span2" style="margin-left:50px">
						<form class="navbar-form navbar-right" role="form" method="post"action="index.php">
						<button type="submit" name="viewUsers"  class="btn btn-defualt">View Accounts</button>
						</form>
					</div>
					<div class="span2" >
						<form class="navbar-form navbar-right" role="form" method="post"action="index.php">
						<button type="submit" name="viewExercise"  class="btn btn-defualt">View Workouts</button>
						</form>
					</div>
					<div class="span2" style="">
						<form class="navbar-form navbar-right" role="form" method="post"action="index.php">
						<button type="submit" name="editUser" class="btn btn-defualt">Edit &nbsp Account</button>
						</form>
					</div>
					<div class="span2" >
						<form class="navbar-form navbar-right" role="form" method="post"action="index.php">
						<button type="submit" name="editExercise"  class="btn btn-defualt">Edit Workouts</button>
						</form>						
					</div>
					<div class="span2" >
						<form class="navbar-form navbar-right" role="form" method="post"action="index.php">
						<button type="submit" name="deleteSection"  class="btn btn-defualt">Delete Section</button>
						</form>						
					</div>
					</div>
					<br><br><br>
					<?php 		
						if(isset($_POST['viewUsers'])){
							include_once "view_users.php";
						
								;
						}
						else if(isset($_POST['viewExercise'])){
							include_once "view_exercises.php";
						
						
								;
						}
						else{
							include_once "view_exercises.php";
							if (isset($_SESSION['username'])){
								include_once "deleteExercise.php";
							}
					
								;
						}?>
					<br>
					<br>
			</div>
			
			
			
			
		<div class="span3">
			<?php 
			if(isset($_POST['search'])){
				include_once "searchresults.php";
			}
			else{
				echo $middleBox ;
			}?>
		</div>
		<div class="span3">
			<?php echo $rightBox ;?>
		</div>
		</div>
		
		
		<div class='navbar navbar-fixed-top'>
			<div class='navbar-inner'>
				<div class='container-fluid'>
					<a class='brand'><?php echo $appName;?> </a>
					<div class="navbar-form pull-right">
						<div class="navbar-form pull-left"> 
							<?php echo "<font color='red'>" . $authenticationErrorMessage. "</font>"; ?>
							
						</div>
						<div class="navbar-form pull-right"> <?php echo $loginBox; ?> </div>
					</div>
				</div>
			</div>
		</div>

	</div>
	<div class='navbar navbar-fixed-bottom'>
	<div class='navbar-inner'>
				<div class='container-fluid'>
		<div class="container"><div class='brand'><?php echo $footer;?></div></div>
	</div>
	</div>
	</div>
	</footer>
	
</body>
</html>
