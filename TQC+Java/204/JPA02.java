import java.util.Scanner;

public class JPA02 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int x = 0, y = 0;

		try {
			x = scanner.nextInt();
			y = scanner.nextInt();
			if (x > 100 || x <= 0 || y > 100 || y <= 0) {
				System.out.print("error");
				return;
			}

		} catch (Exception e) {
			System.out.print("error");
			return;
		}
		int c = 0;
		for (int i = x; i <= y; i++) {
			for (int j = 1; j <= i; j++)
				if (i % j == 0)
					c++;
			if (c == 2)
				System.out.println(i);
			c = 0;
		}
	}
}
