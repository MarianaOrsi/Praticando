public class ServicoDownloadProxy implements Download {

    @Override
    public void solicitarDowload(Usuario usuario) {

        if(usuario.isPremium() == true){
            new ServicoDowload().solicitarDowload(usuario);
        } else {
            System.out.println("O plano do usuario não é premium");
        }

    }
}
