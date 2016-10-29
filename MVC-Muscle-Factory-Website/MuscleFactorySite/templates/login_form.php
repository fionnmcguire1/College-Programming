
<form class="navbar-form navbar-right" role="form" method="post"
	action="index.php" autocomplete="off">
	<div class="form-group">
		<input id='action' type='hidden' name='action' value='loginUser' /> 
		<input
			type="text" name="Username" maxlength="30" required class="form-control"
			placeholder="Username">
		<input type="password" name="Password"
			maxlength="20" required class="form-control" placeholder="password">
		<button type="submit" class="btn btn-primary">Login</button>
	</div>
</form>
