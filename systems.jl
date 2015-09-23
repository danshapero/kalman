
function Lorenz(sigma, rho, beta)
    function F(t::Float64, q::Vector{Float64})
        [sigma * (q[2] - q[1]),
         q[1] * (rho - q[3]) - q[2],
         q[1] * q[2] - beta * q[3]]
    end
end

