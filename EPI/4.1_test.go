package epi

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func testParity(t *testing.T) {

	cases := []struct {
		input int
		want  int
	}{
		{
			input: 0b1010,
			want:  0,
		},
	}

	for _, c := range cases {
		got := parity(c.input)
		assert.Equal(t, c.want, got)
	}

}
