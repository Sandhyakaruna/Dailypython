
import java.util.Scanner;

public class StringMatcher {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        String str1 = sc.nextLine();
        String str2 = sc.nextLine();
        
        String regexPattern = str1.replace("*", ".*").replace("?", ".");
        
        System.out.println("Second string: " + str2);
        
        if (str2.matches(regexPattern)) {
            System.out.println("The strings match");
        } else {
            System.out.println("The strings do not match");
        }
        
        sc.close();
    }
}
