function [theta, J_history] = gradientDescentMulti(X, y, theta, alpha, num_iters)
%GRADIENTDESCENTMULTI Performs gradient descent to learn theta
%   theta = GRADIENTDESCENTMULTI(x, y, theta, alpha, num_iters) updates theta by
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);

for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCostMulti) and gradient here.
    %

    x = X(:,2:3);
    h = theta(1) + (theta(2)*x(:,1)) + (theta(3)*x(:,2));

    theta_zero = theta(1) - alpha * pinv(m) * sum(h - y);
    theta_one  = theta(2) - alpha * pinv(m) * sum((h - y) .* x(:,1));
    theta_two  = theta(3) - alpha * pinv(m) * sum((h - y) .* x(:,2));

    theta = [theta_zero; theta_one; theta_two];

    % ============================================================

    % Save the cost J in every iteration    
    J_history(iter) = computeCostMulti(X, y, theta);

endfor

end
