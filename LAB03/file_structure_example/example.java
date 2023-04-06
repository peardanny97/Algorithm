import java.io.*;
import java.util.Scanner;
 

public class example { 
    public static void main(String[] args) { 
        try {
            Scanner scanner = new Scanner(new File(args[0]));
            Writer pw = new FileWriter(args[1]);
            int a, b, result = 0; 
            a = scanner.nextInt(); b = scanner.nextInt();
            if (args[2].equals("add")) {
                result = a + b;
            }
            else if (args[2].equals("sub")) {
                result = a - b;
            }
            pw.write(String.valueOf(result));
            pw.close();
        }  catch (FileNotFoundException e) {
            e.printStackTrace();
        } finally {
            return ;
        }
        
    }
}
