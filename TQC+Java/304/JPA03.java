import java.util.Scanner;

public class JPA03 {

	public static void main(String[] args) {

		int[] scores = { 100, 100, 95, 95, 92, 91, 90, 100, 88, 88, 87, 87, 90, 91, 85, 80, 81, 82, 82, 89 };
		Scanner scanner = new Scanner(System.in);
		int n = 0;
		try {
			n = scanner.nextInt();
		} catch (Exception e) {
			scanner.next();
		}
		scanner.close();

		double s = 0;
		int c = 0;
		for (int i = 0; i < scores.length; i++)
			if (scores[i] != n) {
				s += scores[i];
				c++;
			}
		System.out.printf("%.2f", s / c);
	}
}