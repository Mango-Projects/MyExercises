import java.util.Scanner;

public class JPA01 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int n1 = 0, n5 = 0, n10 = 0;

		try {
			n1 = Math.max(scanner.nextInt(), 0);
		} catch (Exception e) {
			scanner.next();
		}
		try {
			n5 = Math.max(scanner.nextInt(), 0);
		} catch (Exception e) {
			scanner.next();
		}
		try {
			n10 = Math.max(scanner.nextInt(), 0);
		} catch (Exception e) {
			scanner.next();
		}

		System.out.printf("%,d", n1 + n5 * 5 + n10 * 10);
	}
}
