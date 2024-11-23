import java.util.Scanner;

public class JPA02 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		try {
			int number1 = 25;
			int number2 = scanner.nextInt();
			if (number2 > 25) {
				System.out.print("error");
				return;
			}
			System.out.println(number1 / number2);

		} catch (ArithmeticException error) {
			System.out.print("error:DivideByZeroException");
		} catch (Exception error) {
			System.out.print("error");
		}
	}
}