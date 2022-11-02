public class CheckQuallityLote extends CheckQuallity {

    @Override
    public void verificar(Produto produto) {

        if(produto.getLote() >= 1000 & produto.getLote() <= 2000){
            System.out.println("O lote do produto " + produto.getNome() + " foi aprovado!");
            if(this.getCheckQuallitySeguinte() != null){
                this.getCheckQuallitySeguinte().verificar(produto);
            }
        }else{
            System.out.println("Produto " + produto.getNome() + " Rejeitado! o lote " + produto.getLote() + " não está no limite \n");

        }
    }
}
