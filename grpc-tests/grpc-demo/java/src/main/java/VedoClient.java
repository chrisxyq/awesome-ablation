import com.chrisxyq.GetMeshPointsRequest;
import com.chrisxyq.GetMeshPointsResult;
import com.chrisxyq.VedoGrpc;
import com.helloworld.HelloWorldClient;
import com.zhj.grpc.HelloReply;
import com.zhj.grpc.HelloRequest;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import io.grpc.StatusRuntimeException;
import org.omg.CORBA.INTERNAL;

import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.concurrent.TimeUnit;

public class VedoClient {
    private static final Logger logger = Logger.getLogger(HelloWorldClient.class.getName());

    private final ManagedChannel    channel;
    private final VedoGrpc.VedoBlockingStub blockingStub;

    /**
     * Construct client connecting to HelloWorld server at {@code host:port}.
     */
    public VedoClient(String host, int port) {

        channel = ManagedChannelBuilder.forAddress(host, port)
                .usePlaintext()
                .build();
        blockingStub = VedoGrpc.newBlockingStub(channel);
    }

    public void shutdown() throws InterruptedException {
        channel.shutdown().awaitTermination(5, TimeUnit.SECONDS);
    }

    /**
     * Say hello to server.
     */
    public void greet(int index) {
        GetMeshPointsRequest request = GetMeshPointsRequest.newBuilder().setMeshIndex(index).build();
        GetMeshPointsResult response;
        try {
            response = blockingStub.getMeshPoints(request);
        } catch (StatusRuntimeException e) {
            logger.log(Level.WARNING, "RPC failed: {0}", e.getStatus());
            return;
        }
        logger.info("response.getMeshPoints(): " + response.getMeshPoints());
    }

    /**
     * Greet server. If provided, the first element of {@code args} is the name to use in the
     * greeting.
     */
    public static void main(String[] args) throws Exception {
        VedoClient client = new VedoClient("localhost", 50051);
        try {

            String user = "world";
            if (args.length > 0) {
                user = args[0];
            }
            client.greet(1);
        } finally {
            client.shutdown();
        }
    }
}
