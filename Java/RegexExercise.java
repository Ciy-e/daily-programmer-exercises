
/**
 * 
 * Regex Exercise for username matching.
 * Constraints:
 * Valid usernames are of [a-z], [A-Z], [0-9] and '_'
 * Usernames must begin with an alphabetic character.
 * Usernames must be between 8 and 30 characters in length
 */

import java.util.Scanner;
class RegexExercise {
    public static final String regularExpression = "[A-Za-z][\\w]{7,29}";

    private static final Scanner scan = new Scanner(System.in);
    
    public static void main(String[] args) {
        int n = Integer.parseInt(scan.nextLine());
        while (n-- != 0) {
            String userName = scan.nextLine();

            if (userName.matches(UsernameValidator.regularExpression)) {
                System.out.println("Valid");
            } else {
                System.out.println("Invalid");
            }           
        }
    }
}
