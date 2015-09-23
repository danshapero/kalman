
function Lorenz(sigma, rho, beta)
    function F(t, q)
        [sigma * (q[2] - q[1]);
         q[1] * (rho - q[3]) - q[2];
         q[1] * q[2] - beta * q[3]]
    end
end

