import java.util.Locale;

public class Main {
    public static void main(String[] args) {
        double x = 32.6905;
        System.out.println(x);
        System.out.printf("%.2f%n", x);
        Locale.setDefault(Locale.US);
    }
} 