import java.util.Scanner;

public class JPA04 {
	static Scanner scanner = new Scanner(System.in);

	public static void main(String[] args) {
		try {
			String[] input = scanner.next().split(":");
			int hours = Integer.parseInt(input[0]);
			int minutes = Integer.parseInt(input[1]);

			if (minutes > 59) {
				System.out.print("error");
				return;
			}
			System.out.printf("%dd:%dh:%dm", (int) (hours / 8), hours % 8, minutes);

		} catch (Exception ex) {
			System.out.print("error");
			return;
		}
	}
}