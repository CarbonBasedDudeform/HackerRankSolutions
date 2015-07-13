import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner s = new Scanner(System.in);
        int numTestCases = s.nextInt();
        for (int tests = 0; tests < numTestCases; tests++) {
            int timestamp1 = s.nextInt();
            int timestamp2 = s.nextInt();

            List<Integer> ints = new ArrayList();

            for (int i = 0; i < 10; i++) {
                ints.add(s.nextInt());
            }

            int correctTimestamp = timestamp1;

            while (correctTimestamp <= timestamp2) {
                Random rand = new Random();
                rand.setSeed(correctTimestamp);

                Boolean found = true;
                for (int i = 0; i < 10; i++) {
                    int temp = rand.nextInt(1000);
                    if ( temp != ints.get(i)) {
                        found = false;
                        break;
                    }
                }

                if (found == false) {
                    correctTimestamp++;
                } else{
                    break;
                }
            }

            Random r = new Random();
            r.setSeed(correctTimestamp);
            System.out.print(correctTimestamp + " ");
            //toss away the first ten
            for (int i = 0; i < 10; i++) {
                r.nextInt(1000);
            }

            for (int i = 0; i < 10; i++) {
                System.out.print(r.nextInt(1000) + " ");
            }

            System.out.print("\n");
        }
    }
}
