using System;
using System.Globalization;

namespace Retangulo {
    class Program {
        static void Main(string[] args) {

            CultureInfo CI = CultureInfo.InvariantCulture;

            double area, perimetro, diagonal, base1, altura;

            Console.Write("Base do retangulo: ");
            base1 = double.Parse(Console.ReadLine(), CI);
            Console.Write("Altura do retangulo: ");
            altura = double.Parse(Console.ReadLine(), CI);

            area = base1 * altura;
            perimetro = 2 * (base1 + altura);
            diagonal = Math.Sqrt(Math.Pow(base1, 2.0) + Math.Pow(altura, 2.0));

            Console.WriteLine("AREA = " + area.ToString("F4", CI));
            Console.WriteLine("PERIMETRO = " + perimetro.ToString("F4", CI));
            Console.WriteLine("DIAGONAL = " + diagonal.ToString("F4", CI));


        }
    }
}
