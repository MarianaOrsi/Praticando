public class ProcessaQuallity {
    public static void main(String[] args) {
        Produto produto1 = new Produto("Macarrão", 100, 1910, "Saudavel");
        Produto produto2 = new Produto("Bolo", 1200, 1910, "Saudavel");
        Produto produto3 = new Produto("Pão", 1200, 1300, "Variado");
        Produto produto4 = new Produto("Café", 1000, 1250, "Quase Saudavel");

        CheckProduto checkProduto = new CheckProduto();
        checkProduto.Verificar(produto1);
        checkProduto.Verificar(produto2);
        checkProduto.Verificar(produto3);
        checkProduto.Verificar(produto4);
    }
}
