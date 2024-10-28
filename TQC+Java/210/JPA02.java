import java.util.Scanner;

public class JPA02 {

	public static void main(String[] args) {

		try {
			Scanner scanner = new Scanner(System.in);
			int num1 = 25;
			int num2 = scanner.nextInt();
			scanner.close();
			if (num2 > 25) {
				System.out.print("error");
				return;
			}
			System.out.println(num1 / num2);

		} catch (ArithmeticException e) {
			System.out.print("error:DivideByZeroException");
		} catch (Exception e) {
			System.out.print("error");
		}
	}

}