<?php
define('FILE_PATH', './input.txt');
/**
 * Solves the puzzle
 *
 *@return floor - the solution for the puzzle
 */
function gameSolver()
{   // Santa tracker
    $floor = 0;
    // Position tracker for part 2 of the puzzle
    $position = 1;
    // If file exists get the solution
    if (file_exists(FILE_PATH)) {
        $fStream =  fopen(FILE_PATH, 'r');
        // loop through each character in the file
        while(!feof($fStream)) {
            // Store the character in a variable
            $char = fgetc($fStream);
            if (strcmp($char,'(') == 0) {
                echo '(';
                $floor++;
            } elseif(strcmp($char,')') == 0) {
                echo ')';                
                $floor--;
                // Added for the part 2 of the puzzle
                partTwo($floor, $position);
            }
            $position++;
        }
        fclose($fStream );
    } else {
        echo "Error: File doesn't exist" . PHP_EOL;
        return;
    }
    return $floor;
}

/**
  *Solution for part 2 of the puzzle
  *
  *@param $floor - the current floor level
  *@param $position - the position of the command
  */
function partTwo($floor, $position) {
    if ($floor == -1) {
        echo $position;
    }
}

/**
 * The main function
 */
function main() {
    // Get the solution
    $solution = gameSolver();
    // If no errors occur print the solution
    if($solution != null) {
        echo $solution;
    }
}

main();
?>