<h3 style="color:white">Delete Exercise</h3>
<legend>Enter ID of Exercise to Delete</legend>
<form action="index.php" method="post">
	<fieldset>
		<input id='action' type='hidden' name='action' value='deleteExercise' />
		<p>
				Exercise: <input type="number" id="ex_id" name="exercise_id" min=0 placeholder="Exercise ID" maxlength="20"  />
		</p>
		<p>
		<div class="form-group">
			<div class="controls">
				<button type="submit" class="btn btn-success">Delete</button>
			</div>
		</div>
		</p>
	</fieldset>
</form>