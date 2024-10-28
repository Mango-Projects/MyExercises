import java.util.Scanner;

public class JPA01 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int x = 0, y = 0;

		try {
			x = scanner.nextInt();
		} catch (Exception error) {
			x = 0;
		}
		try {
			y = scanner.nextInt();
		} catch (Exception error) {
			y = 0;
		}
		scanner.close();

		if (x % 2 == 0 && y % 2 == 0)
			System.out.println(x + y);
		else
			System.out.println(0);
	}
}
