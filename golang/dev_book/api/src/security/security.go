package security

import "golang.org/x/crypto/bcrypt"

func Hash(passwd string) ([]byte, error) {
	return bcrypt.GenerateFromPassword([]byte(passwd), bcrypt.DefaultCost)
}

func HashVerify(stringPass, hashPass string) error {
	return bcrypt.CompareHashAndPassword([]byte(hashPass), []byte(stringPass))
}