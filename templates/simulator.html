<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Disease Solutions-Simulation</title>
<meta name="keywords" content="" />
<meta name="description" content="" />
<link href="../static/epidemic/tooplate_style.css" rel="stylesheet" type="text/css" />
<!--   Free Website Template by t o o p l a t e . c o m   -->
<script language="javascript" type="text/javascript">
function clearText(field)
{
    if (field.defaultValue == field.value) field.value = '';
    else if (field.value == '') field.value = field.defaultValue;
}
</script>

</head>
<body>

<div id="tooplate_wrapper">

	<div id="tooplate_header">

        <div id="tooplate_menu">
        	<ul>
                <li><a href="/epidemic/epidemic" >Home</a></li>
                <li><a href="/epidemic/aboutus">About Us</a></li>
				<li><a href="/epidemic/demographics">Demographics</a></li>
                <li><a href="/epidemic/simulator" class="current">Simulation</a></li>
				<li><a href="/epidemic/policies">Policies</a></li>
                <li><a href="/epidemic/contact2">Contact</a></li>
            </ul>
            <div class="cleaner"></div>
        </div> <!-- end of menu -->
        <br></br>
		<div id="site_title"><h1><strong>Disease Solutions</strong><br></br><span>Leaders in Disaster Mitigation</span></h1></div>

    </div> <!-- end of header -->

    <div id="tooplate_middle">

	<!-- This is in here for the wave picture to show up from the CSS file -->

    </div> <!-- end of middle -->

	<div id="tooplate_main">
		<br></br>
		<h3>Disease Spread Simulation</h3>
		<p>Select from the following parameters to model a disease spread in the Greater Lafayette area</p>
		<?php
			$servername = "mydb.ics.purdue.edu";
			$username = "g1081391";
			$password = "Wif1hasnomeaning";
			$dbname = "g1081391";

			// Create connection
			$conn = new mysqli($servername, $username, $password, $dbname);

			// Check connection
			if ($conn->connect_error) {
				die("Connection failed: " . $conn->connect_error);
			}

			$sql = "SELECT Region_Num FROM Region";
			$result = $conn->query($sql);

		?>
		<!-- This section creates the drop down menus to select the network simulation stats to show-->
		<form id="contactForm" action = "simulator.php" method="post">
		<table class="order">
		<tr><td></td></tr>
		<h5>Disease Type</h5>
		<p><i>The four diseases included below are used as a reference for different types of diseases.</i></p>
		<ul><i>
			<li>"Flu" represents diseases that have lower infectivity and very low mortality.</li>
			<li>"Smallpox" represents diseases that have a medium infectivity and medium mortality.</li>
			<li>"Measles" represents diseases that have an extremely high infectivity but low mortality.</li>
			<li>"Ebola" represents diseases that have a low infectivity but extremely high mortality.</li>
		</i></ul>
		<p><i>See the graph below for comparisons of more diseases in terms of infectivity and mortality rates.</i></p>

		<img style="border:4px solid black" src="../static/epidemic/images/gallery/microbe.jpg" width="870px" border: "#000000 6px outset"/>
		<br></br>

		<select name="Disease" style="width:200px">
			<option selected="selected" disabled="disabled">Select disease type</option>
			<option value="1">Flu</option>
			<option value="2">Smallpox</option>
			<option value="3">Measles</option>
			<option value="4">Ebola</option>
		</select>
		<br></br>
		<h5>Initial Number Infected</h5>
		<p><i>The following simulations will be based on the selected number of individuals being infected with the disease. To match what policy makers will know before an outbreak begins, those individuals will be selected at random from the population.</i></p>
		<select name="infectNum" style="width:200px">
			<option selected="selected" disabled="disabled">Select initial number infected</option>
			<option value="1">1 individual</option>
			<option value="3">3 individuals</option>
			<option value="10">10 individuals</option>
		</select>
		<br></br>
		<h5>Percentage of K-Nodes to Select</h5>
		<p><i>This represents the percentage of the population you wish to tailor your policies to. The lower the percentage, the more you are focusing on those that make the grestest impact on the disease spread.</i></p>
		<select name="kNodes" style="width:200px">
			<option selected="selected" disabled="disabled">Select percentage to consider</option>
			<option value="0.1">Focused approach: 10%</option>
			<option value="0.3">Balanced approach: 30% </option>
			<option value="0.6">Broadest approach: 60%</option>
		</select>
		<br></br>
		<input type="submit" name="hit" value="Select" />
		</form>
		<br></br>
		</table>

		<?php
			// Determines if request has been submitted
			if(isset($_POST['hit'])){
				$disease = $_POST['Disease'];
				$infectNum = $_POST['infectNum'];
				$kNodes = $_POST['kNodes'];
				// If statements to determine which case was chosen based on drop down menu options
				// Case 1
				if ($disease == 1 && $infectNum == 1 && $kNodes == 0.1){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case1.gif"/>'; // Displays gif of disease spread for given parameters
					echo'<img src="../static/epidemic/images/decisionTrees/Case1.png"/>'; // Displays image of pruned decision tree for disease spread
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 125,431<br>
					Max Infected at a Time: 42,274<br>
					Total Recovered: 124,057<br>
					Total Dead: 1,373<br>
					Susceptible After 100 Days: 15,201<br>
					Cost per Vaccine Dose: $12.30<br>
					Total Vaccination Cost (Based on K-Node Selection): $154,280<br></em>";
				}
				// Case 2
				else if ($disease == 1 && $infectNum == 1 && $kNodes == 0.3){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case2.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case2.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 125,583<br>
					Max Infected at a Time: 42,844<br>
					Total Recovered: 124,226<br>
					Total Dead: 1,353<br>
					Susceptible After 100 Days: 15,049<br>
					Cost per Vaccine Dose: $12.30<br>
					Total Vaccination Cost (Based on K-Node Selection): $463,401<br></em>";
				}
				// Case 3
				else if ($disease == 1 && $infectNum == 1 && $kNodes == 0.6){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case3.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case3.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 125,609<br>
					Max Infected at a Time: 41,548<br>
					Total Recovered: 124,236<br>
					Total Dead: 1,364<br>
					Susceptible After 100 Days: 15,023<br>
					Cost per Vaccine Dose: $12.30<br>
					Total Vaccination Cost (Based on K-Node Selection): $926,994<br></em>";
				}
				// Case 4
				else if ($disease == 1 && $infectNum == 3 && $kNodes == 0.1){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case4.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case4.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 125,463<br>
					Max Infected at a Time: 42,358<br>
					Total Recovered: 124,085<br>
					Total Dead: 1,375<br>
					Susceptible After 100 Days: 15,169<br>
					Cost per Vaccine Dose: $12.30<br>
					Total Vaccination Cost (Based on K-Node Selection): $154,320<br></em>";
				}
				// Case 5
				else if ($disease == 1 && $infectNum == 3 && $kNodes == 0.3){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case5.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case5.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 125,595<br>
					Max Infected at a Time: 42,583<br>
					Total Recovered: 124,241<br>
					Total Dead: 1,346<br>
					Susceptible After 100 Days: 15,037<br>
					Cost per Vaccine Dose: $12.30<br>
					Total Vaccination Cost (Based on K-Node Selection): $463,456<br></em>";
				}
				// Case 6
				else if ($disease == 1 && $infectNum == 3 && $kNodes == 0.6){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case6.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case6.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 125,585<br>
					Max Infected at a Time: 42,831<br>
					Total Recovered: 124,197<br>
					Total Dead: 1,384<br>
					Susceptible After 100 Days: 15,047<br>
					Cost per Vaccine Dose: $12.30<br>
					Total Vaccination Cost (Based on K-Node Selection): $926,817<br></em>";
				}
				// Case 7
				else if ($disease == 1 && $infectNum == 10 && $kNodes == 0.1){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case7.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case7.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 125,686<br>
					Max Infected at a Time: 42,670<br>
					Total Recovered: 124,250<br>
					Total Dead: 1,430<br>
					Susceptible After 100 Days: 14,946<br>
					Cost per Vaccine Dose: $12.30<br>
					Total Vaccination Cost (Based on K-Node Selection): $154,594<br></em>";
				}
				// Case 8
				else if ($disease == 1 && $infectNum == 10 && $kNodes == 0.3){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case8.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case8.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 125,716<br>
					Max Infected at a Time: 43,062<br>
					Total Recovered: 124,338<br>
					Total Dead: 1,376<br>
					Susceptible After 100 Days: 14,916<br>
					Cost per Vaccine Dose: $12.30<br>
					Total Vaccination Cost (Based on K-Node Selection): $463,892<br></em>";
				}
				// Case 9
				else if ($disease == 1 && $infectNum == 10 && $kNodes == 0.6){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case9.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case9.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 125,315<br>
					Max Infected at a Time: 42,434<br>
					Total Recovered: 123,955<br>
					Total Dead: 1,358<br>
					Susceptible After 100 Days: 15,317<br>
					Cost per Vaccine Dose: $12.30<br>
					Total Vaccination Cost (Based on K-Node Selection): $924,825<br></em>";
				}
				// Case 10
				else if ($disease == 2 && $infectNum == 1 && $kNodes == 0.1){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="images/cases/Case10.gif"/>';
					echo'<img src="images/decisionTrees/Case10.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 139,505<br>
					Max Infected at a Time: 76,387<br>
					Total Recovered: 59,187<br>
					Total Dead: 79,920<br>
					Susceptible After 100 Days: 1,127<br>
					Cost per Vaccine Dose: $3.00<br>
					Total Vaccination Cost (Based on K-Node Selection): $41,852<br></em>";
				}
				// Case 11
				else if ($disease == 2 && $infectNum == 1 && $kNodes == 0.3){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case11.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case11.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 139,487<br>
					Max Infected at a Time: 80,396<br>
					Total Recovered: 59,500<br>
					Total Dead: 79,623<br>
					Susceptible After 100 Days: 1,145<br>
					Cost per Vaccine Dose: $3.00<br>
					Total Vaccination Cost (Based on K-Node Selection): $125,538<br></em>";
				}
				// Case 12
				else if ($disease == 2 && $infectNum == 1 && $kNodes == 0.6){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case12.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case12.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 139,541<br>
					Max Infected at a Time: 79,791<br>
					Total Recovered: 58,894<br>
					Total Dead: 80,292<br>
					Susceptible After 100 Days: 1,091<br>
					Cost per Vaccine Dose: $3.00<br>
					Total Vaccination Cost (Based on K-Node Selection): $251,174<br></em>";
				}
				// Case 13
				else if ($disease == 2 && $infectNum == 3 && $kNodes == 0.1){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case13.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case13.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 139,446<br>
					Max Infected at a Time: 78,891<br>
					Total Recovered: 59,314<br>
					Total Dead: 79,756<br>
					Susceptible After 100 Days: 1,186<br>
					Cost per Vaccine Dose: $3.00<br>
					Total Vaccination Cost (Based on K-Node Selection): $41,834<br></em>";
				}
				// Case 14
				else if ($disease == 2 && $infectNum == 3 && $kNodes == 0.3){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case14.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case14.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 139,470<br>
					Max Infected at a Time: 80,161<br>
					Total Recovered: 59,355<br>
					Total Dead: 79,752<br>
					Susceptible After 100 Days: 1,162<br>
					Cost per Vaccine Dose: $3.00<br>
					Total Vaccination Cost (Based on K-Node Selection): $125,523<br></em>";
				}
				// Case 15
				else if ($disease == 2 && $infectNum == 3 && $kNodes == 0.6){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case15.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case15.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 139,504<br>
					Max Infected at a Time: 79,097<br>
					Total Recovered: 59,584<br>
					Total Dead: 79,573<br>
					Susceptible After 100 Days: 1,128<br>
					Cost per Vaccine Dose: $3.00<br>
					Total Vaccination Cost (Based on K-Node Selection): $251,107<br></em>";
				}
				// Case 16
				else if ($disease == 2 && $infectNum == 10 && $kNodes == 0.1){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case16.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case16.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 139,424<br>
					Max Infected at a Time: 79,654<br>
					Total Recovered: 59,528<br>
					Total Dead: 79,554<br>
					Susceptible After 100 Days: 1,208<br>
					Cost per Vaccine Dose: $3.00<br>
					Total Vaccination Cost (Based on K-Node Selection): $41,827<br></em>";
				}
				// Case 17
				else if ($disease == 2 && $infectNum == 10 && $kNodes == 0.3){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case17.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case17.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 139,498<br>
					Max Infected at a Time: 76,347<br>
					Total Recovered: 59,658<br>
					Total Dead: 79,468<br>
					Susceptible After 100 Days: 1,134<br>
					Cost per Vaccine Dose: $3.00<br>
					Total Vaccination Cost (Based on K-Node Selection): $125,548<br></em>";
				}
				// Case 18
				else if ($disease == 2 && $infectNum == 10 && $kNodes == 0.6){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case18.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case18.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 139,438<br>
					Max Infected at a Time: 77,037<br>
					Total Recovered: 59,647<br>
					Total Dead: 79,461<br>
					Susceptible After 100 Days: 1,194<br>
					Cost per Vaccine Dose: $3.00<br>
					Total Vaccination Cost (Based on K-Node Selection): $250,988<br></em>";
				}
				// Case 19
				else if ($disease == 3 && $infectNum == 1 && $kNodes == 0.1){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case19.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case19.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 140,567<br>
					Max Infected at a Time: 100,856<br>
					Total Recovered: 135,743<br>
					Total Dead: 4,824<br>
					Susceptible After 100 Days: 65<br>
					Cost per Vaccine Dose: $42.12<br>
					Total Vaccination Cost (Based on K-Node Selection): $592,068<br></em>";
				}
				// Case 20
				else if ($disease == 3 && $infectNum == 1 && $kNodes == 0.3){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case20.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case20.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 140,564<br>
					Max Infected at a Time: 104,013<br>
					Total Recovered: 135,725<br>
					Total Dead: 4,839<br>
					Susceptible After 100 Days: 68<br>
					Cost per Vaccine Dose: $42.12<br>
					Total Vaccination Cost (Based on K-Node Selection): $1,776,167<br></em>";
				}
				// case 21
				else if ($disease == 3 && $infectNum == 1 && $kNodes == 0.6){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case21.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case21.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 140,574<br>
					Max Infected at a Time: 106,016<br>
					Total Recovered: 135,734<br>
					Total Dead: 4,839<br>
					Susceptible After 100 Days: 58<br>
					Cost per Vaccine Dose: $42.12<br>
					Total Vaccination Cost (Based on K-Node Selection): $3,552,586<br></em>";
				}
				// Case 22
				else if ($disease == 3 && $infectNum == 3 && $kNodes == 0.1){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case22.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case22.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 140,560<br>
					Max Infected at a Time: 104,252<br>
					Total Recovered: 135,776<br>
					Total Dead: 4,784<br>
					Susceptible After 100 Days: 72<br>
					Cost per Vaccine Dose: $42.12<br>
					Total Vaccination Cost (Based on K-Node Selection): $592,039<br></em>";
				}
				// Case 23
				else if ($disease == 3 && $infectNum == 3 && $kNodes == 0.3){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case23.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case23.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 140,554<br>
					Max Infected at a Time: 105,149<br>
					Total Recovered: 135,624<br>
					Total Dead: 4,927<br>
					Susceptible After 100 Days: 78<br>
					Cost per Vaccine Dose: $42.12<br>
					Total Vaccination Cost (Based on K-Node Selection): $1,776,040<br></em>";
				}
				// Case 24
				else if ($disease == 3 && $infectNum == 3 && $kNodes == 0.6){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case24.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case24.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 140,559<br>
					Max Infected at a Time: 104,159<br>
					Total Recovered: 135,731<br>
					Total Dead: 4,828<br>
					Susceptible After 100 Days: 73<br>
					Cost per Vaccine Dose: $42.12<br>
					Total Vaccination Cost (Based on K-Node Selection): $3,552,207<br></em>";
				}
				// Case 25
				else if ($disease == 3 && $infectNum == 10 && $kNodes == 0.1){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case25.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case25.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 140,562<br>
					Max Infected at a Time: 103,744<br>
					Total Recovered: 135,724<br>
					Total Dead: 4,837<br>
					Susceptible After 100 Days: 70<br>
					Cost per Vaccine Dose: $42.12<br>
					Total Vaccination Cost (Based on K-Node Selection): $592,047<br></em>";
				}
				// Case 26
				else if ($disease == 3 && $infectNum == 10 && $kNodes == 0.3){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case26.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case26.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 140,566<br>
					Max Infected at a Time: 105,923<br>
					Total Recovered: 135,810<br>
					Total Dead: 4,756<br>
					Susceptible After 100 Days: 66<br>
					Cost per Vaccine Dose: $42.12<br>
					Total Vaccination Cost (Based on K-Node Selection): $1,776,192<br></em>";
				}
				// Case 27
				else if ($disease == 3 && $infectNum == 10 && $kNodes == 0.6){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case27.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case27.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 140,571<br>
					Max Infected at a Time: 105,244<br>
					Total Recovered: 135,663<br>
					Total Dead: 4,908<br>
					Susceptible After 100 Days: 61<br>
					Cost per Vaccine Dose: $42.12<br>
					Total Vaccination Cost (Based on K-Node Selection): $3,552,510<br></em>";
				}
				// Case 28
				else if ($disease == 4 && $infectNum == 1 && $kNodes == 0.1){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case28.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case28.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 1<br>
					Max Infected at a Time: 1<br>
					Total Recovered: 0<br>
					Total Dead: 1<br>
					Susceptible After 100 Days: 140,631<br>
					*Note: due to the high mortality of this disease, the simulation found that the single individual infected died before transmitting it to others.
					Cost per Vaccine Dose: $135.90<br>
					Total Vaccination Cost (Based on K-Node Selection): $135.90<br></em>";
				}
				// Case 29
				else if ($disease == 4 && $infectNum == 1 && $kNodes == 0.3){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case29.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case29.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 79,938<br>
					Max Infected at a Time: 11,472<br>
					Total Recovered: 37,589<br>
					Total Dead: 42,347<br>
					Susceptible After 100 Days: 60,694<br>
					Cost per Vaccine Dose: $135.90<br>
					Total Vaccination Cost (Based on K-Node Selection): $3,259,072<br></em>";
				}
				// Case 30
				else if ($disease == 4 && $infectNum == 1 && $kNodes == 0.6){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case30.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case30.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 1<br>
					Max Infected at a Time: 1<br>
					Total Recovered: 0<br>
					Total Dead: 1<br>
					Susceptible After 100 Days: 140,631<br>
					*Note: due to the high mortality of this disease, the simulation found that the single individual infected died before transmitting it to others.
					Cost per Vaccine Dose: $135.90<br>
					Total Vaccination Cost (Based on K-Node Selection): $135.90<br></em>";
				}
				// Case 31
				else if ($disease == 4 && $infectNum == 3 && $kNodes == 0.1){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case31.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case31.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 79,550<br>
					Max Infected at a Time: 12,208<br>
					Total Recovered: 37,223<br>
					Total Dead: 42,336<br>
					Susceptible After 100 Days: 61,082<br>
					Cost per Vaccine Dose: $135.90<br>
					Total Vaccination Cost (Based on K-Node Selection): $1,081,085<br></em>";
				}
				// Case 32
				else if ($disease == 4 && $infectNum == 3 && $kNodes == 0.3){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case32.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case32.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 79,981<br>
					Max Infected at a Time: 11,745<br>
					Total Recovered: 37,590<br>
					Total Dead: 42,391<br>
					Susceptible After 100 Days: 60,651<br>
					Cost per Vaccine Dose: $135.90<br>
					Total Vaccination Cost (Based on K-Node Selection): $3,260,825<br></em>";
				}
				// Case 33
				else if ($disease == 4 && $infectNum == 3 && $kNodes == 0.6){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case33.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case33.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 79,152<br>
					Max Infected at a Time: 12,417<br>
					Total Recovered: 37,364<br>
					Total Dead: 41,788<br>
					Susceptible After 100 Days: 61,480<br>
					Cost per Vaccine Dose: $135.90<br>
					Total Vaccination Cost (Based on K-Node Selection): $6,454,054<br></em>";
				}
				// Case 34
				else if ($disease == 4 && $infectNum == 10 && $kNodes == 0.1){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case34.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case34.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 79,772<br>
					Max Infected at a Time: 12,620<br>
					Total Recovered: 37,499<br>
					Total Dead: 42,273<br>
					Susceptible After 100 Days: 60,860<br>
					Cost per Vaccine Dose: $135.90<br>
					Total Vaccination Cost (Based on K-Node Selection): $1,084,101<br></em>";
				}
				// Case 35
				else if ($disease == 4 && $infectNum == 10 && $kNodes == 0.3){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case35.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case35.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 80,009<br>
					Max Infected at a Time: 12,922<br>
					Total Recovered: 37,735<br>
					Total Dead: 42,273<br>
					Susceptible After 100 Days: 60,623<br>
					Cost per Vaccine Dose: $135.90<br>
					Total Vaccination Cost (Based on K-Node Selection): $3,261,967<br></em>";
				}
				// Case 36
				else if ($disease == 4 && $infectNum == 10 && $kNodes == 0.6){
					echo'<h5>Results:</h5>';
					echo"<br>";
					echo'<img src="../static/epidemic/images/cases/Case36.gif"/>';
					echo'<img src="../static/epidemic/images/decisionTrees/Case36.png"/>';
					echo"<br><br><h5>Final Statistics:</h5>
					<em>Total Number Infected: 80,049<br>
					Max Infected at a Time: 12,711<br>
					Total Recovered: 37,456<br>
					Total Dead: 42,584<br>
					Susceptible After 100 Days: 60,592<br>
					Cost per Vaccine Dose: $135.90<br>
					Total Vaccination Cost (Based on K-Node Selection): $6,526,462<br></em>";
				}
				// This is to make sure they can't just hit the select button.
				else {
					echo'<em>Please select options from the drop down menus to see simulation results.</em>';
				}
			}

		echo "<br><br>";
		?>

		<p><i>For information about what policies to consider, please <a href="../static/epidemic/policies.php">click here.</a><br></br>

	</div>	<!-- end of main -->

    <div id="tooplate_footer">

        Copyright © 2018 <em>Disease Solutions</em>

    </div> <!-- end of tooplate_footer -->

</div> <!-- end of wrapper -->
<!--   Free Website Template by t o o p l a t e . c o m   -->
</body>
</html>
