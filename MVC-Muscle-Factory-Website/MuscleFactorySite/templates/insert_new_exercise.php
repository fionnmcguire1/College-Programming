<h3 style='color:white' > New Exercises<br></h3><h2 style='color:cyan'><legend>Add Your Own Exercise</legend></h2>
<form action="index.php" method="post">
	<fieldset>
		<input id='action' type='hidden' name='action' value='insertNewExercise' />
		<p>
			<label for="ex_name">Exercise Name:</label> <input type="text"
				id="ex_name" name="ex_name" placeholder="Exercise Name"
				maxlength="25" required />
		</p>
		<p>
			<label for="ex_desc">Description</label> <input type="text"
				id="ex_desc" name="ex_desc" placeholder="Description"
				maxlength="25" required />
		</p>
		<p>
			<label for="type">Type of exercise:</label> <input type="number"
				id="type" name="type" placeholder="Type" min="0" max="6" required />
		</p>
		
		<p>
		<div class="form-group">
			<div class="controls">
				<button type="submit" class="btn btn-success">Add</button>
			</div>
		</div>
		</p>
	</fieldset>
</form>


