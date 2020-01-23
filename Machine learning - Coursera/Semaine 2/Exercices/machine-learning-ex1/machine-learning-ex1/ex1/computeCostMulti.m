function J = computeCostMulti(X, y, theta)
%COMPUTECOSTMULTI Compute cost for linear regression with multiple variables
%   J = COMPUTECOSTMULTI(X, y, theta) computes the cost of using theta as the
%   parameter for linear regression to fit the data points in X and y

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta
%               You should set J to the cost.

for i = 2:size(X,2)
  
  X(:,i)
  predictions(:,i) = X(:,i)*theta;             % predictions of hypothesis on examples
  squaredErrors(:,i) = (predictions - y).^2; % squared errors

  J(:,i) = pinv(2*m) * sum(squaredErrors(:,i));
  
endfor

% =========================================================================

end
