import java.util.Scanner;

enum colors {
	RED, BLUE, WHITE
}

class Car {
	int cc, seat, door;
	colors color;
}

public class JPA06 {
	public static void main(String args[]) {
		try {
			Scanner scanner = new Scanner(System.in);
			String[] input = scanner.nextLine().split(" ");
			scanner.close();

			System.out.printf("%scc%s%s%s", input[0], input[1], colors.values()[Integer.parseInt(input[2])-1], input[3]);
		} catch (Exception ex) {
			System.out.print("error");
			return;
		}
	}
}
