public class ServicoDowload implements Download {

    @Override
    public void solicitarDowload(Usuario usuario) {
        System.out.println("O plano do usuario é " + usuario.getPlano() + ". Baixando");
    }
}
