package basics.tutorial;
import java.util.Scanner;
public class ScannerTest {
	public static void main( String[] args ){
		Scanner scanner = new Scanner(System.in);
		System.out.print("Please input a number ");
		int a = scanner.nextInt();
		System.out.printf("The square of %d is %d", a, a*a);
		
	}

}
