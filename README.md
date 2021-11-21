
 
# Project Repository

In this repository, you'll work on your homework assignments and submit your completed project for review by the TAs.

### Please remember:
1. Your Source Code should be located under src folder.
2. In this ReadMe, add assumptions, screenshots, comments, and other requirements
3. Delete all unnecessary source code or test files under src or test folders.
4. coverage.xml is used to get the test coverage statistics and you don't need to worry about editing it.
5. sonar-properties file is used for SonarQube statistics and you don't need to worry about editing it as well.
6. You will find code design checklist under docs/ folder. You may use it as a reference for implementing best code practices.

For several of the variables in players_20.csv, we assume variable character type. Date of birth is documented as "date" data type. Anything that isn't varchar(n) or date is "integer" or "text" data type. 

### Fifa Table Infrastructure 
Below is a partial summary of my Fifa table infrastructure. 
![image](https://user-images.githubusercontent.com/69126128/139150872-9087639f-98c6-48ba-976e-d44bdc56eac3.png)

### Running the Application 
Below, I will describe the steps to get my application running. 

#### Step 1
To create the tables in SQL for Player20 and Player 19, the following SQL queries were used.<br />

CREATE TABLE fifa.players20 (
	sofifa_id integer,
	player_url text,
	short_name text,
	long_name text,
	age integer,
	dob date,
	height_cm integer,
	weight_kg integer,
	nationality text,
	club text,
	overall integer,
	potential integer,
	value_eur integer,
	wage_eur integer,
	player_positions text,
	preferred_foot varchar(5),
	international_reputation integer,
	weak_foot integer,
	skill_moves integer,
	work_rate text,
	body_type text,
	real_face varchar(3),
	release_clause_eur integer,
	player_tags text,
	team_position varchar(3),
	team_jersey_number integer,
	loaned_from text,
	joined date,
	contract_valid_until integer,
	nation_position varchar(3),
	nation_jersey_number integer,
	pace integer,
	shooting integer,
	passings integer,
	dribbling integer,
	defending integer,
	physic integer, 
	gk_diving integer, 
	gk_handling integer,
	gk_kicking integer,
	gk_reflexes integer,
	gk_speed integer,
	gk_positioning integer, 
	player_traits text,
	attacking_crossing integer,
	attacking_finishing integer, 
	attacking_heading_accuracy integer, 
	attacking_short_passing integer, 
	attacking_volleys integer,
	skill_dribbling integer,
	skill_curve integer, 
	skill_fk_accuracy integer, 
	skill_long_passing integer,
	skill_ball_control integer, 
	movement_acceleration integer, 
	movement_sprint_speed integer, 
	movement_agility integer, 
	movement_reactions integer, 
	movement_balance integer, 
	power_shot_power integer, 
	power_jumping integer, 
	power_stamina integer, 
	power_strength integer, 
	power_long_shots integer, 
	mentality_aggression integer, 
	mentality_interceptions integer, 
	mentality_positioning integer, 
	mentality_vision integer, 
	mentality_penalties integer, 
	mentality_composure integer, 
	defending_marking integer, 
	defending_standing_tackle integer, 
	defending_sliding_tackle integer, 
	goalkeeping_diving integer, 
	goalkeeping_handling integer,
	goalkeeping_kicking integer, 
	goalkeeping_positioning integer, 
	goalkeeping_reflexes integer,
	ls text,
	st text,
	rs text,
	lw text,
	lf text,
	cf text,
	rf text,
	rw text,
	lam text,
	cam text,
	ram text,
	lm text,
	lcm text,
	cm text,
	rcm text,
	rm text,
	lwb text,
	ldm text,
	cdm text,
	rdm text,
	rwb text,
	lb text,
	lcb text,
	cb text,
	rcb text,
	rb text 
);

CREATE TABLE fifa.players19 (
	sofifa_id integer,
	player_url text,
	short_name text,
	long_name text,
	age integer,
	dob date,
	height_cm integer,
	weight_kg integer,
	nationality text,
	club text,
	overall integer,
	potential integer,
	value_eur integer,
	wage_eur integer,
	player_positions text,
	preferred_foot varchar(5),
	international_reputation integer,
	weak_foot integer,
	skill_moves integer,
	work_rate text,
	body_type text,
	real_face varchar(3),
	release_clause_eur integer,
	player_tags text,
	team_position varchar(3),
	team_jersey_number integer,
	loaned_from text,
	joined date,
	contract_valid_until integer,
	nation_position varchar(3),
	nation_jersey_number integer,
	pace integer,
	shooting integer,
	passings integer,
	dribbling integer,
	defending integer,
	physic integer, 
	gk_diving integer, 
	gk_handling integer,
	gk_kicking integer,
	gk_reflexes integer,
	gk_speed integer,
	gk_positioning integer, 
	player_traits text,
	attacking_crossing text,
	attacking_finishing text, 
	attacking_heading_accuracy text, 
	attacking_short_passing text, 
	attacking_volleys text,
	skill_dribbling text,
	skill_curve text, 
	skill_fk_accuracy text, 
	skill_long_passing text,
	skill_ball_control text, 
	movement_acceleration text, 
	movement_sprint_speed text, 
	movement_agility text, 
	movement_reactions text, 
	movement_balance text, 
	power_shot_power text, 
	power_jumping text, 
	power_stamina text, 
	power_strength text, 
	power_long_shots text, 
	mentality_aggression text, 
	mentality_interceptions text, 
	mentality_positioning text, 
	mentality_vision text, 
	mentality_penalties text, 
	mentality_composure text, 
	defending_marking text, 
	defending_standing_tackle text, 
	defending_sliding_tackle text, 
	goalkeeping_diving text, 
	goalkeeping_handling text,
	goalkeeping_kicking text, 
	goalkeeping_positioning text, 
	goalkeeping_reflexes text
);

#### Step 2
After creating the tables, import the CSV files into their respective tables with the following queries. You will need to download the CSV files that are in the "data" folder with the files "players_20.csv" and "players_19.csv". Make sure you set your permissions for the directory where your CSV files are as "everyone", or you may run into some permission errors and not be able to import the data into the SQL tables. The port number for my postgres database is 5432.<br />

copy players 
from 'C:/Users/emily/Documents/CMU MSP/stat 650/final project/data/players_20.csv'
delimiter ',' csv header;

copy players 
from 'C:/Users/emily/Documents/CMU MSP/stat 650/final project/data/players_19.csv'
delimiter ',' csv header;

If there are issues with the tables being in the wrong schema i.e. not in the fifa schema, you can use the following query.<br />

alter table players20
	set schema fifa;

#### Step 3
After you import the data into the postgres tables, you can run the entire Python script (there is a "main.py" and "final project.ipynb" file) in the "src" folder. Make sure you have the Python modules "psycopg2" and "pandas" installed before runnning the script. If you don't have these modules installed, you can run "pip install pscycopg2" or "pip install pandas" in your terminal. I personally use Jupyter Notebook to run Python, so I would recommend running the .ipynb file, so you can see the notebook chunks for better readability. For questions 1, 2, 3, you can input an integer value into the function's argument (for question 3, z must be greater than or equal to 5).<br /> 

### Unit Testing 
Refer to the "test" folder to see what unit tests I ran for each of the the 5 Python functions I created. In the following paragraphs, I describe a summary of all the test scenarios I went through for each function.<br /> 

#### Function 1
For function 1, I assessed whether the function is returning anything. Then I assessed that the function is returning the right number of elements. I also assessed to see if the first element was the right element and made sure that the first element didn't return the wrong element. Lastly, I checked to make sure my error message inside my function was working properly.<br />

#### Function 2
For function 2, I assessed whether the function is returning anything. Then I assessed that the function is returning the right number of elements. I also assessed to see if the first element was the right element and made sure that the first element didnt' return the second element. Additionally, I assessed that the ordering of the elements was correct. Lastly, I checked to make sure my error message inside my function was working properly.

#### Function 3
For function 3, I assessed whether the function is returning anything. Then I assessed that the function is returning the right number of elements. Then I assessed to see whether the error messages inside my function were working correctly. I also checked to see that the elements that are returned were in the right order. 

#### Function 4
For function 4, I had two Python functions, so i developed 2 unit test functions that are essentially the same assertion statement. First, I assessed whether the function is returning anything. Then I assessed that the function is returning the right number of elements. Lastly, I assessed that the first element was returning the right thing. 

#### Function 5
For function 5, I assessed whether the function is returning anything. Then I assessed that the function is returning the right number of elements. Lastly, I assessed that the first element was returning the right thing. 
