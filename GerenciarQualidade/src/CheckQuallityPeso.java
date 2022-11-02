public class CheckQuallityPeso extends CheckQuallity {

    @Override
    public void verificar(Produto produto) {
        if(produto.getPeso() >= 1200 & produto.getPeso() <= 1300){
            System.out.println("O peso do produto " + produto.getNome() + " foi aprovado!");
            if(this.getCheckQuallitySeguinte() != null){
                this.getCheckQuallitySeguinte().verificar(produto);
            }
        }else{
            System.out.println("Produto " + produto.getNome() + " Rejeitado! o peso " + produto.getPeso() + " não está no limite \n");

        }
    }
}
